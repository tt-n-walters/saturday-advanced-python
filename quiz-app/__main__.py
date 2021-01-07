import os
import logging

from .quiz import Quiz
from .attempt import Attempt

# Set parent directory
directory_name = os.path.dirname(os.path.abspath(__file__))
os.chdir(directory_name)


logging.basicConfig(filename="quiz.log", level=logging.DEBUG, format="%(asctime)s :::: %(levelname)s :::: %(msg)s")

logging.info("App starting.")
quiz = Quiz()
attempt = Attempt(quiz, number_of_questions=3, show_answers=False)
attempt.choose_category()

logging.debug("Asking questions.")
attempt.start()
logging.info("App finished.")