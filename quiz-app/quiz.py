import time
import os

from .category import Category


# Quiz class with a data structure to hold all category objects
class Quiz:
    def __init__(self):
        category_names = [
            "animals", "brain-teasers", "celebrities", "entertainment",
            "for-kids", "general", "geography", "history", "hobbies",
            "humanities", "literature",  "movies", "music", "newest",
            "people", "rated", "religion-faith", "science-technology",
            "sports", "television", "video-games", "world"
        ]
        self.categories = { name: None for name in category_names }


    @staticmethod
    def get_category_timestamp(category_name):
        with open("cache/{}".format(category_name), "r", encoding="utf-8") as file:
            timestamp = next(file)
            return int(timestamp)


    def get_category(self, category_name):
        filename = "cache/{}".format(category_name)

        # Category not yet cached
        if not os.path.exists(filename):
            category = Category.download(category_name)
        # Cache out of date
        elif Quiz.get_category_timestamp(category_name) + 30 < time.time():
            category = Category.download(category_name)
        # Read from cache
        else:
            category = Category.from_cache(category_name)
        
        self.categories[category_name] = category
        return category
