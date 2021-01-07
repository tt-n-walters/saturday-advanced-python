import requests
import random
import time

from .question import Question


class Category:
    def __init__(self, name, questions_text):
        self.name = name
        self.questions = []
        self.process_questions(questions_text)
    

    @classmethod
    def from_cache(cls, name):
        filename = "cache/{}".format(name)
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
        return cls(name, contents)


    @classmethod
    def download(cls, name):
        url = "https://raw.githubusercontent.com/uberspot/OpenTriviaQA/master/categories/{}".format(name)
        response = requests.get(url)
        if not response.status_code == 200:
            exit("Category download failed. {}".format(response.status_code))
        else:
            print("Category download succeeded.")
            with open("cache/{}".format(name), "w", encoding="utf-8") as file:
                timestamp = round(time.time())
                file.write(str(timestamp))
                file.write(response.text)
        return cls(name, response.text)
        
    
    def process_questions(self, text):
        # Remove any extra empty space at the beginning or end of the text,
        # and split into questions
        raw_questions = text.strip().split("#Q")

        # Ignore the first question_string as it is empty, and process the rest
        for question_string in raw_questions[1:]:
            q_object = Question(question_string.strip())
            self.questions.append(q_object)
        
        print("Processed {} questions.".format(len(self.questions)))


    def random_question(self):
        number = random.randint(0, len(self.questions) - 1)
        return self.questions[number]

        number = random.randrange(0, len(self.questions))
        return self.questions[number]

        return random.choice(self.questions)
