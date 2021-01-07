
class Attempt:
    def __init__(self, quiz, number_of_questions=5, show_answers=False):
        self.quiz = quiz
        self.number_of_questions = number_of_questions
        self.show_answers = show_answers
    

    def choose_category(self):
        category_names = self.quiz.categories.keys()
        print("Choices: " + ", ".join(category_names))
        chosen_category = input("Choose a category: ")
        if chosen_category not in category_names:
            print("Invalid category '" + chosen_category + "'.")
            exit()
        
        self.category = self.quiz.get_category(chosen_category)


    def ask_question(self):
        question = self.category.random_question()

        print(question)
        answer = input("Enter answer: ")
        if question.check_answer(answer):
            print("Correct.")
        else:
            print("Wrong.")
            if self.show_answers:
                print("Correct answer was: " + question.correct)


    def start(self):
        for _ in range(self.number_of_questions):
            self.ask_question()
