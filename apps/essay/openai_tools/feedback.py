import json
from openai_common import model, system_role_in_ielts, open_ai


class FeedbackAI:
    def __init__(self, max_tokens: int = 1000):
        self.max_tokens = max_tokens
        self.temperature = 0

    def generate_feedback(self, topic, essay, letter_type):
        sentence = f"""{system_role_in_ielts}
                      
                        Your output must be a JSON following this structure, 
                        in band section please give minimum and maximum bands in [band_1, band_2] list format  
                        "band": [band_1, band_2], 
                        “coherence and cohesion”: your feedback (maximum 100 words), 
                        “grammatical range”: your feedback (maximum 100 words), 
                        “lexical resource”: your feedback (maximum 100 words),
                        
                        
                        Topic: {topic}

                        Essay: {essay}
                        
                        JSON:
                        """
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
        self.feedback = json.loads(response["choices"][0]["message"]["content"].strip())
        print(self.feedback)


classe = FeedbackAI()

text = """
Children are born into the digital world. From young age, they know how to operate computers, iPad, and TV. It is part of their daily life. School age children is no exception to the use of computers. They are confident users of computers and very dependent on them which can lead to decline in reading and writing skills. Some teachers utilise the computers well in their lessons, while others avoid the use of computers in their classrooms. I believe good balance of both is needed to help students’ reading and writing skills to improve.

Computers can help students with reading. For example, if students come across unknown words, they can search the unknow words and hear the pronunciation. If it was not for the computers, they have to find someone who knows how to pronounce the words for them. Therefore, computers can play positive role in students’ reading skills.

On the other hands, writing skills need to be improved by lots of handwritten works. If students are using computers all the time and getting the help of autocorrection, they will not improve their writing skills. They will not know how to edit as autocorrect is doing the job for them.

In conclusion, I believe that teachers should not allow students to do all the work on the computers especially writing tasks. However, teacher should not avoid the use of computer as computers can be a great help if they use it effectively. Rather than avoiding computers that students are so used to, teachers need to come up with how to use it effectively to enhance students’ reading and writing skills.

"""

topic = "School children are becoming far too dependent on computers and this is having an alarming effect on reading and writing skills. Teachers need to avoid using computers in the classroom at all costs and go back to teaching basic study skills. To what extent do you agree or disagree?"
classe.generate_feedback(essay=text, topic=topic, letter_type=None)


