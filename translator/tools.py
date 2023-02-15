import json

import exceptions
from scraping import Scraper

with open('data.json', 'r', encoding='utf-8') as data:
    languages = json.load(data)['languages']


class Translator:

    def __init__(self):
        self.source = None
        self.target = None
        self.word = None

    def _write_to_file(self, target, words, examples):
        # creating a text file named word.txt, where 'word'
        # is the word that was being translated, and appending
        # the results in a readable format
        with open(f'{self.word}.txt', 'a', encoding='utf-8') as file:
            file.write(
                f"{target.capitalize()} Translations:\n" +
                "{}\n{}\n{}".format(*words) + '\n\n' +
                f"{target.capitalize()} Examples:\n" +
                "{}\n{}\n\n{}\n{}\n".format(*examples) + '\n\n'
            )

    def translate(self, source: str, target: str, word: str):
        self.source = source.lower()
        self.target = target.lower()
        self.word = word.lower()

        # checking if source and target languages are valid,
        # if not, raising the user-defined exception
        try:
            if source not in languages:
                raise exceptions.UnableToFindLanguageError(self.source)
            if target not in languages + ['all']:
                raise exceptions.UnableToFindLanguageError(self.target)
        except exceptions.UnableToFindLanguageError as err:
            raise SystemExit(err)

        if self.target == 'all':
            # if target is 'all', the translation will be 
            # applied to every language
            for target_lang in languages:
                if target_lang != self.source:  # except the source
                    scraper = Scraper(self.source, target_lang, self.word)
                    words, examples = scraper.scrape()

                    # checking if the word is a valid word
                    try:
                        # word is not valid if the 'words' list created
                        # by the Scraper has the length not equal to 3,
                        # because there must be 3 word translations
                        if len(words) != 3:
                            # raising the user-defined exception
                            raise exceptions.UnableToFindWordError(self.word)
                    except exceptions.UnableToFindWordError as err:
                        raise SystemExit(err)

                    self._write_to_file(target_lang, words, examples)
        else:
            scraper = Scraper(self.source, self.target, self.word)
            words, examples = scraper.scrape()
            
            try:
                if not words or len(words) == 1:
                    raise exceptions.UnableToFindWordError(self.word)
            except exceptions.UnableToFindWordError as err:
                raise SystemExit(err)

            self._write_to_file(self.target, words, examples)

    def get_translations(self) -> str:
        # reading and returning the file that was created in translate() method
        with open(f'{self.word}.txt', 'r', encoding='utf-8') as file:
            return file.read()
