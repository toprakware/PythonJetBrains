from argparse import ArgumentParser

from text import TextAttributes
import tests


def main():
    parser = ArgumentParser(description="Readability Tester")
    parser.add_argument('file_path', help="path to the text file that will be tested")
    args = parser.parse_args()

    with open(f'{args.file_path}', 'r', encoding='utf-8') as file:
        text = file.read()

    attributes = TextAttributes(text)

    ARI_test = tests.AutomatedIndex(
        chars=attributes.n_chars,
        sentences=attributes.n_sentences,
        words=attributes.n_words
    )

    FKR_test = tests.FleschKincaidTest(
        syllables=attributes.n_syllables,
        sentences=attributes.n_sentences,
        words=attributes.n_words
    )

    DCI_test = tests.DaleChallIndex(
        difficult=attributes.n_difficult,
        sentences=attributes.n_sentences,
        words=attributes.n_words
    )

    print("Text: {}\n".format(text))
    print(attributes)
    print("\n---- TEST RESULTS ----\n")
    print(ARI_test)
    print(FKR_test)
    print(DCI_test)

    average_age = round((ARI_test.get_age_avg() + FKR_test.get_age_avg() + DCI_test.get_age_avg()) / 3, 1)
    print("This text should be understood in average by {} year olds.".format(average_age))


if __name__ == '__main__':
    main()
