import json
from openai_common import open_ai, model, system_role_in_ielts


class TaskResponseAI:
    def __init__(self, max_tokens: int = 1000):
        self.max_tokens = max_tokens
        self.temperature = 0

    def task_response(self, topic, letter_type):
        sentence = f"""{system_role_in_ielts}

                        Your output must be a JSON following this structure, 
                        write ielts essay in provided topic , it must be at least 250 words or maximum 300 words 
                        “essay”: your essay (maximum 300 words),

                        Topic: {topic}

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
        self.task_response = json.loads(response["choices"][0]["message"]["content"].strip())
        print(self.task_response)

# classe = TaskResponseAI()
# topic = "School children are becoming far too dependent on computers and this is having an alarming effect on reading and writing skills. Teachers need to avoid using computers in the classroom at all costs and go back to teaching basic study skills. To what extent do you agree or disagree?"
# classe.task_response(topic=topic, letter_type=None)




def find_cohesion_coherence_words_in_essay(essay, topic):
    sentence = f"""{system_role_in_ielts}

                           Your output must be a JSON following this structure, 
                           find connecting words from essay and return this words , do not include same word twice in list
                           
                           data : [word,]

                           Topic: {topic}
                           essay: {essay}
                           
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
        max_tokens=1000,
        temperature=0,
    )
    task_response = json.loads(response["choices"][0]["message"]["content"].strip())
    print(task_response)

text = """
Children are born into the digital world. From young age, they know how to operate computers, iPad, and TV. It is part of their daily life. School age children is no exception to the use of computers. They are confident users of computers and very dependent on them which can lead to decline in reading and writing skills. Some teachers utilise the computers well in their lessons, while others avoid the use of computers in their classrooms. I believe good balance of both is needed to help students’ reading and writing skills to improve.

Computers can help students with reading. For example, if students come across unknown words, they can search the unknow words and hear the pronunciation. If it was not for the computers, they have to find someone who knows how to pronounce the words for them. Therefore, computers can play positive role in students’ reading skills.

On the other hands, writing skills need to be improved by lots of handwritten works. If students are using computers all the time and getting the help of autocorrection, they will not improve their writing skills. They will not know how to edit as autocorrect is doing the job for them.

In conclusion, I believe that teachers should not allow students to do all the work on the computers especially writing tasks. However, teacher should not avoid the use of computer as computers can be a great help if they use it effectively. Rather than avoiding computers that students are so used to, teachers need to come up with how to use it effectively to enhance students’ reading and writing skills.

"""

topic = "School children are becoming far too dependent on computers and this is having an alarming effect on reading and writing skills. Teachers need to avoid using computers in the classroom at all costs and go back to teaching basic study skills. To what extent do you agree or disagree?"

find_cohesion_coherence_words_in_essay(text, topic)


