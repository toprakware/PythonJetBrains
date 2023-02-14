from argparse import ArgumentParser

from tools import Translator


def main():
    parser = ArgumentParser(description="Multilingual Online Translator Program")
    parser.add_argument('source', help="the language of the word that will be translated")
    parser.add_argument('target', help="the language that the word will be translated into")
    parser.add_argument('word', help="the word that will be translated")
    args = parser.parse_args()

    translator = Translator()
    translator.translate(args.source, args.target, args.word)

    translations = translator.get_translations()
    print(translations)


if __name__ == "__main__":
    main()
