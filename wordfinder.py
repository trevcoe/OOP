"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def init(you, path):
        dict_file = open(path)
        you.words = you.parse(dict_file)
        print(f"{len(you.words)} words read")

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(you):
        return random.choice(you.words)