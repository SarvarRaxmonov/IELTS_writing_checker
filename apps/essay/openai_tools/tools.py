import time

import language_tool_python
import enchant
import spacy
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet
from dataclasses import dataclass
from rich import print

@dataclass
class Tools:
    essay: str = ""

    def __init__(self, essay):
        self.essay = essay
        self.split_essay = self.essay.split()
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = self.nlp(self.essay)

    def tool_paragraph_word_sentence_count(self):
        sentences = sent_tokenize(self.essay)
        words = self.split_essay
        average_sentence_length = len(words) / len(sentences)

        data = {
            "num_paragraphs": self.essay.count("\n\n"),
            "num_sentences": len(sentences),
            "num_average_sentence": int(average_sentence_length),
            "num_words": len(words),
        }
        return data

    def tool_adjective_adverb_words(self):
        adjectives = set([word.text for word in self.doc if word.pos_ == "ADJ"])
        adverbs = set([word.text for word in self.doc if word.pos_ == "ADV"])
        data = dict(adjectives=adjectives, adverbs=adverbs)
        return data

    def tool_repetitive_words(self):
        excluded_word_types = [
            "ADP",
            "AUX",
            "DET",
            "INTJ",
            "PART",
            "PRON",
            "PROPN",
            "PUNCT",
            "SYM",
            "SPACE",
        ]
        repeated_words = dict()
        list_format_of_essay = (
            self.essay.replace(",", "").replace(".", "").replace("!", "").split()
        )
        for word in self.doc:
            if (
                word.pos_ not in excluded_word_types
                and not word.is_stop
                and list_format_of_essay.count(word.text) > 2
                and word.text not in repeated_words.keys()
            ):
                repeated_words[word.text] = self.tool_get_synonyms(word.text)
        return repeated_words

    def tool_spell_checker(self):
        essay = self.essay.replace(",", " ").replace(".", " ").replace("’", "")
        misspelled_words = dict()
        dictionary = enchant.Dict("en_US")
        words = essay.split()
        for word in words:
            if not dictionary.check(word):
                misspelled_words[word] = dictionary.suggest(word)[:3]
        return misspelled_words

    def tool_get_synonyms(self, word):
        return list(
            set(
                [
                    lemma.name().replace("_", " ")
                    for syn in wordnet.synsets(word)
                    for lemma in syn.lemmas()
                    if lemma.name() != word
                ]
            )
        )[:4]

    def tool_compound_sentences(self):
        compound_sentences = set([str(word) for word in self.doc if word.dep_ == "cc"])
        return list(compound_sentences)

    def tool_subordinating_clause(self):
        subordinate_clauses = []
        for sentence in self.doc.sents:
            for token in sentence:
                if token.dep_ == "mark":
                    subordinate_clauses.append([sentence.text, token.text])
        return subordinate_clauses

    def tool_grammar_check(self):
        tool = language_tool_python.LanguageTool("en-US")
        matches = tool.check(self.essay)
        incorrect_grammar = {match.context: match.replacements for match in matches}
        return incorrect_grammar

text = """
The concept of creating vertical cities with towering skyscrapers to accommodate urban expansion has been proposed, and in some cases, materialised in many cities around the world. While there are benefits to this approach, it also presents several disadvantages, and this essay will explore both.

One of the key advantages of vertical cities is their potential to maximize land usage efficiently. With limited available land for urban growth, constructing tall buildings allows for increased population density without further encroaching on natural spaces. For instance, cities like Hong Kong and New York have embraced vertical living to accommodate their growing populations while preserving green spaces and minimizing urban sprawl.

Another benefit lies in the potential reduction of commuting times. Vertical cities can centralize various services and amenities within close proximity, minimizing the need for extensive travel within the city. Residents can easily access workplaces, shopping centres, and recreational facilities without enduring long commutes. This efficiency in commuting can contribute to improved work-life balance and reduced environmental pollution.

However, the drawbacks of living in vertical cities should not be overlooked. Tall buildings can create a sense of isolation and disconnect among residents due to limited outdoor spaces and a lack of community areas. The absence of shared public spaces like parks and open squares may hinder social interactions and impede the development of a cohesive urban community. For instance, studies have shown that high-rise living can lead to feelings of loneliness and social detachment among residents.

Furthermore, the overreliance on vertical expansion could lead to environmental concerns. Tall buildings require extensive energy consumption for heating, cooling, and vertical transportation systems. The sheer height of these structures can exacerbate the urban heat island effect and increase energy consumption, potentially offsetting the environmental benefits of reducing horizontal urban sprawl.

In conclusion, vertical cities with towering buildings revolve around a range of advantages and disadvantages. While efficient land use and reduced commuting times are potential benefits, concerns related to community cohesion, social interaction, and environmental sustainability warrant careful consideration when planning for such urban developments.

"""


t = Tools(essay=text)
print(t.tool_adjective_adverb_words(),
t.tool_compound_sentences(),
t.tool_grammar_check(),
t.tool_paragraph_word_sentence_count(),
t.tool_repetitive_words(),
t.tool_spell_checker(),
t.tool_subordinating_clause())


