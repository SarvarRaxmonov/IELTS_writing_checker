from dataclasses import dataclass


@dataclass
class Gpt_Chat_Messages:
    topic: str = ""
    essay: str = ""
    letter_type: str = "formal"
    with_additional_details: bool = False

    def cohesion_and_sentence_variety(self):
        cohesion_and_sentence_variety = f"""Please analyze the provided essay for cohesion and sentence variety.
    
        Return the following information in JSON format:
    
        {{
        "data": [
                {{
                    "cohesion": 'one word description',
                    "sentence_variety": 'one word description'
                }}
            ]
        }}
    
        Topic: {self.topic}
    
        Essay:
        {self.essay}
    
        JSON:"""
        return cohesion_and_sentence_variety

    def cohesion_words(self):
        cohesion_words = f"""
        Retrieve sentences containing strong cohesive devices from the essay. Cohesive devices encompass words or phrases that signal connections between paragraphs or sections within a text or speech. These devices include References, Conjunctions, Linking Words and Phrases, Ellipsis, Substitution, and Parallelism. Please exclude any sentences lacking cohesive devices and refrain from returning the entire essay or any descriptive content.
        
        If the essay does not have any cohesive devices like 'however,' 'therefore,' etc., then return an empty list. You don't need to find the cohesive devices from every essay.
        
        Returning format example, return as a JSON object:
        {{
            "note": 'cohesion_coherence_note' (Generate concise notes on cohesion and coherence based on the provided essay. Cohesion pertains to the grammatical and lexical elements that connect sentences and paragraphs, ensuring a smooth flow of ideas. Coherence, on the other hand, relates to the logical arrangement and clarity of these ideas. Please provide a summary of these concepts without including the entire essay.),
            "list": [
                {{
                    "cohesive_device": 'cohesive_device_1',
                    "sentence": 'sentence_1'
                }},
        
                {{
                    "cohesive_device": 'cohesive_device_2',
                    "sentence": 'sentence_2'
                }},
            ]
        }}
        
        Essay:
        {self.essay}
        """
        return cohesion_words

    def correlative_sentences_msg(self):
        correlative_sentences = f"""
       A correlative sentence typically involves the use of pairs of correlative conjunctions .
       These pairs of words are used to connect elements in a sentence, often to show alternatives, contrasts, or equal importance. 
       Additionally, please demonstrate how to identify and extract correlative sentences and their associated correlative conjunctions from a given essay.
       
       - It's important that the information is correct and not misleading !
       - The found correlative conjunction must be in sentence !
                                 
       Return the following information in JSON format:
        
        {{
            "data": [
                {{
                    'word': 'correlative conjunction' # example data : 'either...or',
                    'sentence': 'sentence' # sentence which correlative conjunction is used 
                }},
            ],
        }}
        
        Essay:
        {self.essay}
        
        JSON:
        """
        return correlative_sentences

    def improved_words_msg(self):
        improved_words = f"""
        Identify and suggest improvements for words that need enhancement. Focus on the most essential ones to enrich the vocabulary, not all of them.
        
        Example:
        
        data: [
            {{
                "chosen word": ['improved word', 'improved word'],
                "chosen word": ['improved word', 'improved word'],
                ...
            }},
        ],
        
        Return the following information in JSON format:
        
        {{
            "data": [
                {{
                    "chosen word": ['improved word'],
                }},
            ],
        }}
        
        Essay:
        {self.essay}
        
        JSON:
        """

        return improved_words

    def task_response_essay_msg(self):
        task_response = f"""
        Your output must be a JSON following this structure, 
        write ielts essay in provided topic , it must be at least 250 words or maximum 300 words 
        “essay”: your essay (maximum 300 words),
    
        Topic: {self.topic}
    
        JSON:
        """
        return task_response

    def task_response_letter_msg(self):
        task_response_letter = f"""
        Your output must be a JSON following this structure, 
        write IELTS Letter General Training Writing Task 1 using provided topic , it must be at least 150 words or maximum 300 words 
        “essay”: your essay (maximum 300 words),
    
        Topic: {self.topic}
        Letter Type: {self.letter_type}
        JSON:
        """
        return task_response_letter

    def feedback_of_essay_msg(self):
        additional_data_of_feedback_essay = ""
        essay_explanation = ""
        if self.with_additional_details:
            essay_explanation = "please provide accurately band for each criteria of this essay it would be 'coherence and cohesion' or others . # 'coherence and cohesion': [['• answer', ], [6]]"
            additional_data_of_feedback_essay = "[band of this criteria] # example 'criteria name': [['• answer', ], [6]] "

        feedback_of_essay = f"""
                               Your output must be a JSON following this structure, 
                               - In the "band" section, please provide  accurately minimum and maximum bands for the full essay in [band_1, band_2] list format.
                               - Begin your answers to questions with a bullet point ('•'), for example: ['• Answer for the first question', ].
                               - {essay_explanation},    
    
                               Answer the given all questions based on the text:
    
                               "task response" :  questions :
                                                  • Are all parts of the task covered ?,
                                                  • Does your response include well-developed with relevant, extended and supported ideas?,
                                                  • Does it have 250+ words ?, 
    
                               "coherence and cohesion": questions :
                                                  • Is paragraphing proper ?,
                                                  • Is there a clear progression?,
                                                  • Is there a clear central topic in each paragraph?, 
    
                               "grammatical range":  questions : 
                                                  • Are complex sentences used ?,
                                                  • Is there any grammatical errors?,
                                                  • Is punctuation proper?, 
    
                               "lexical resource":  questions : 
                                                  • What are the adjectives, synonyms and antonyms related to the essay topic?
                                                  • Am I repeating same words?
                                                  • Am I making same spelling mistakes again and again?
    
                               example_data : 
                               'data' : [
                                           {{
                                             "band":[5,6],
                                             "overall_feedback": your feedback (maximum 100 words) # note without any mistake details only feedback 
                                           }},
                                           {{
                                             "grammatical range": [['• answer', ], [{additional_data_of_feedback_essay}]],
                                           }},
                                        ]
    
                               Return the following information in JSON format:
    
                                 {{ 
                                     "data": [
                                         {{
                                         "band": [band_1, band_2],
                                         "overall_feedback": your feedback (maximum 100 words) # note without any mistake details only feedback 
                                         }},
                                         {{
                                             "criteria name": [['• answer', ], [{additional_data_of_feedback_essay}]],
                                         }},
                                     ],
                                 }}
    
    
    
                               Topic: {self.topic}
    
                               Essay: {self.essay}
    
                               JSON:
                               """

        return feedback_of_essay

    def feedback_of_letter_msg(self):
        additional_data_of_feedback_letter = ""
        letter_explanation = ""
        if self.with_additional_details:
            letter_explanation = "please provide accurately band for each criteria of this essay it would be 'coherence and cohesion' or others . # 'coherence and cohesion': [['• answer', ], [6]]"
            additional_data_of_feedback_letter = "[band of this criteria] # example 'criteria name': [['• answer', ], [6]] "
        feedback_of_letter = f"""
                              Your output must be a JSON following this structure, 
                              - Begin your answers to questions with a bullet point ('•'), for example: ['• Answer for the first question', ].
                              - {letter_explanation},    
    
                              Answer the given all questions based on the text:
    
                              "task response" :  questions :
                                                • Are all parts of the task covered?
                                                • Is your response well-developed with relevant, extended and supported ideas?
                                                • Does it have 150+ words ?
    
                              "coherence and cohesion": questions :
                                                 • Is paragraphing proper ?
                                                 • Is there a clear progression?
    
                              "grammatical range":  questions : 
                                                 • Are complex sentences used ?
                                                 • Is there any grammatical errors?
                                                 • Is punctuation proper?
    
                              "lexical resource":  questions : 
                                                • What are the adjectives, synonyms and antonyms related to the letter topic?
                                                • Am I repeating same words?
                                                • Am I making same spelling mistakes again and again?
    
                              example_data : 
                              'data' : [
                                          {{
                                            "overall_tone_feedback": your feedback (maximum 100 words) # note without any mistake details only feedback 
                                          }},
                                          {{
                                            "grammatical range": [['• answer', ], [{additional_data_of_feedback_letter}]],
                                          }},
                                       ]
    
                              Return the following information in JSON format:
    
                                {{ 
                                    "data": [
                                        {{
                                        "overall_tone_feedback": your feedback (maximum 100 words) # note without any mistake details only feedback 
                                        }},
                                        {{
                                            "criteria name": [['• answer', ], [{additional_data_of_feedback_letter}]],
                                        }},
                                    ],
                                }}
    
    
    
                              Topic: {self.topic}
    
                              Letter: {self.essay}
                              Letter type : {self.letter_type}
                              JSON:
                              """

        return feedback_of_letter
