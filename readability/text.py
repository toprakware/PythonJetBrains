import nltk
from nltk.tokenize import regexp_tokenize, sent_tokenize

nltk.download('punkt')


class TextAttributes:

    def __init__(self, text: str):
        self.text = text
        self.n_chars = None
        self.n_sentences = None
        self.n_words = None
        self.n_syllables = None
        self.n_difficult = None
        self.set_attributes()

    def __str__(self) -> str:
        return f"Characters: {self.n_chars}\n" + \
               f"Sentences: {self.n_sentences}\n" + \
               f"Words: {self.n_words}\n" + \
               f"Difficult words: {self.n_difficult}\n" + \
               f"Syllables: {self.n_syllables}\n"

    def set_attributes(self):
        self.n_chars = self.get_n_chars()
        self.n_sentences = self.get_n_sentences()
        self.n_words = self.get_n_words()
        self.n_syllables = self.get_n_syllables()
        self.n_difficult = self.get_n_difficult()

    def get_n_chars(self) -> int:
        """ Returns the number of characters in the text"""
        return len(regexp_tokenize(self.text, pattern=r"[^\s]"))
    
    def get_n_sentences(self) -> int:
        """ Returns the number of sentences in the text """
        return len(sent_tokenize(self.text))

    def get_n_words(self) -> int:
        """ Returns the number of words in the text """
        return len(regexp_tokenize(self.text, pattern="[0-9A-z']+"))
    
    def get_n_syllables(self) -> int:
        """ Returns the approximate number of syllables in the text """
        vowels = 'aeiouy'
        syllable_count = 0
        words = [word.lower() for word in regexp_tokenize(self.text, pattern="[0-9A-z']+")]
        
        for word in words:
            if word[0] in vowels:
                syllable_count += 1

            for i in range(1, len(word)):
                if word[i] in vowels and word[i - 1] not in vowels:
                    syllable_count += 1

            if word.endswith('e'):
                syllable_count -= 1

            if word.endswith('le'):
                if len(word) > 2 and word[-3] not in vowels:
                    syllable_count += 1

        return max(syllable_count, 1)

    def get_n_difficult(self) -> int:
        """ Returns the number of difficult words in the text """
        with open('frequents.txt', 'r', encoding='utf-8') as file:
            frequents = [word.strip('\n') for word in file.readlines()]
        words = [word.lower() for word in regexp_tokenize(self.text, pattern=r"[A-z\d']+")]
        
        diff_count = 0
        for word in words:
            for freq in frequents:
                if word == freq:
                    break
            else:
                diff_count += 1

        return diff_count
