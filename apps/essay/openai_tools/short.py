import json
import re

import spacy
import contextualSpellCheck
from spacy import Language
from spacy.pipeline import EntityRuler

from openai_common import open_ai, model
from nltk.tokenize import sent_tokenize



class ShortAI:
    def __init__(self, max_tokens: int = 1000):
        self.max_tokens = max_tokens
        self.temperature = 0

    def generate_cohesion_and_sentence_variety(self, topic, essay, letter_type):
        sentence = f"""Please analyze the provided essay for cohesion and sentence variety. Find and list the repeated words (excluding grammar words) that appear more than twice in the essay.
            
                              Return the following information in JSON format:

                           "  {{ 
                       "data": [
                           {{
                               "cohesion": 'one word description',
                               "sentence_variety": 'one word description'
                               "repeated_words": [['word', 'word_count'],
                           }},
                       ],
                   }}

                   Topic: {topic}

                   Essay:
                   {essay}

                   JSON:"""
        messages = [
                {
                    "role": "system",
                    "content": sentence,
                },
            ]

        response = open_ai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        self.short = json.loads(response["choices"][0]["message"]["content"].strip())
        print(self.short)


text = """
Children are born into the digital world. From young age, they know how to operate computers, iPad, and TV. It is part of their daily life. School age children is no exception to the use of computers. They are confident users of computers and very dependent on them which can lead to decline in reading and writing skills. Some teachers utilise the computers well in their lessons, while others avoid the use of computers in their classrooms. I believe good balance of both is needed to help students’ reading and writing skills to improve.

Computers can help students with reading. For example, if students come across unknown words, they can search the unknow words and hear the pronunciation. If it was not for the computers, they have to find someone who knows how to pronounce the words for them. Therefore, computers can play positive role in students’ reading skills.

On the other hands, writing skills need to be improved by lots of handwritten works. If students are using computers all the time and getting the help of autocorrection, they will not improve their writing skills. They will not know how to edit as autocorrect is doing the job for them.

In conclusion, I believe that teachers should not allow students to do all the work on the computers especially writing tasks. However, teacher should not avoid the use of computer as computers can be a great help if they use it effectively. Rather than avoiding computers that students are so used to, teachers need to come up with how to use it effectively to enhance students’ reading and writing skills.

"""
#
# cv = ShortAI()
# cv.generate_cohesion_and_sentence_variety(
#     topic="Some people believe that entertainers are paid too much and their impact on society is negative, while others disagree and believe that they deserve the money that they make because of their positive effects on society. Discuss both opinions and give your own opinion. ",
#     essay=text,
#     letter_type="formal",
# )


class ShortTools:

    def essay_paragraph_word_sentence_count(self, essay):
        sentences = sent_tokenize(essay)
        words = essay.split()
        average_sentence_length = len(words) / len(sentences)

        data = {
            "num_paragraphs": essay.count("\n\n"),
            "num_sentences": len(sentences),
            "num_average_sentence": int(average_sentence_length),
            "num_words": len(words),
        }
        return data


    def essay_lexical_resource(self, essay):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(essay)
        data = {
        "Adjectives": [word.text for word in doc if word.pos_ == "ADJ"],
        "Adverbs": [word.text for word in doc if word.pos_ == "ADV"]
        }

        # dat = [f"{word.text} {word.pos_}" for word in doc if word.pos_]
        # print(
        #     '\n\n', dat
        # )
        return data
    def essay_repetitive_words(self, essay):
        nlp = spacy.load("en_core_web_sm")
        list_format_of_essay = essay.split()
        doc = nlp(essay)
        excluded_word_types = ["ADP", "AUX", "CONJ", "DET", "INTJ", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "SPACE"]
        only_words = [word.text for word in doc if word.pos_ not in excluded_word_types and list_format_of_essay.count(word.text) > 2]
        return list(set(only_words))

classs = ShortTools()
d = classs.essay_paragraph_word_sentence_count(text)
b = classs.essay_repetitive_words(text)
print(d, b)








