
class Question:
    def __init__(self, question_string):
        # Slice the string from the beginning until the position of the ^ character
        # and removed the extra newline at the end
        text_end_index = question_string.index("^")
        self.text = question_string[0:text_end_index].strip()
        
        def remove_two(string):
            return string[2:]
        
        # Extract the correct anwer and all answers from the question string
        answers_string = question_string[text_end_index:]
        # Remove the first two characters from each line, and then save into the
        # appropriate variables
        self.correct, *self.answers = map(remove_two, answers_string.splitlines())
    

    def __repr__(self):
        prefixes = "abcdefgh"[:len(self.answers)]
        formatted_answers = []
        for prefix, answer in zip(prefixes, self.answers):
            formatted_answers.append(prefix + ": " + answer)
        separator = "\n  "
        return self.text + separator + separator.join(formatted_answers)


    def check_answer(self, prefix):
        answer_index = "abcdefgh".index(prefix)
        answer = self.answers[answer_index]
        return answer == self.correct
