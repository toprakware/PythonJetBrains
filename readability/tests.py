from abc import ABC, abstractmethod
from math import ceil
import json

with open('table.json', 'r', encoding='utf-8') as json_file:
    table = json.load(json_file)['table']


class Test(ABC):
    
    def __init__(self, test_name: str, score: int):
        self.test_name = test_name
        self.score = score
        self.start_age = None
        self.end_age = None
        self.get_ages()

    def __str__(self) -> str:
        return f"{self.test_name}: {self.score}. " + \
                "The text can be understood by " + \
               f"{self.start_age}-{self.end_age} year olds."

    @abstractmethod
    def calculate_score(self):
        """ Calculates the readability score """

    def get_ages(self):
        """ Gets the age borders """
        self.start_age = table[self.score - 1]['start_age']
        self.end_age = table[self.score - 1]['end_age']
    
    def get_age_avg(self) -> int:
        """ Returns the average age """
        return (self.start_age + self.end_age) / 2


class AutomatedIndex(Test):
    
    def __init__(self, chars: int, sentences: int, words: int):
        self.chars = chars
        self.sentences = sentences
        self.words = words

        score = self.calculate_score()
        super(AutomatedIndex, self).__init__("Automated Readability Index", score)

    def __str__(self) -> str:
        return super(AutomatedIndex, self).__str__()

    def calculate_score(self) -> int:
        """
        Calculates the readability score according to
        the Automated Readability Index formula
        """
        score = ceil(
            4.71 * (self.chars / self.words)
            + .5 * (self.words / self.sentences)
            - 21.43
        )

        return score


class FleschKincaidTest(Test):
    
    def __init__(self, syllables: int, sentences: int, words: int):
        self.syllables = syllables
        self.sentences = sentences
        self.words = words

        score = self.calculate_score()
        super(FleschKincaidTest, self).__init__("Flesch-Kincaid Readability Test", score)

    def __str__(self) -> str:
        return super(FleschKincaidTest, self).__str__()

    def calculate_score(self) -> int:
        """
        Calculates the readability score according to
        the Flesch-Kincaid Readability Test formula
        """
        score = ceil(
            .39 * (self.words / self.sentences)
            + 11.8 * (self.syllables / self.words)
            - 15.59
        )

        return score
    

class DaleChallIndex(Test):
    
    def __init__(self, difficult: int, sentences: int, words: int):
        self.difficult = difficult
        self.sentences = sentences
        self.words = words

        score = self.calculate_score()
        super(DaleChallIndex, self).__init__("Dale-Chall Readability Index", score)

    def __str__(self) -> str:
        return super(DaleChallIndex, self).__str__()

    def calculate_score(self) -> int:
        """
        Calculates the readability score according to
        the Dale-Chall Readability Index formula
        """
        score = ceil(
            .1579 * (self.difficult / self.words) * 100
            + .0496 * (self.words / self.sentences)
            + 3.6365
        )

        return score
