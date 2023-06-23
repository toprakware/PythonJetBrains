# Readability Score Tool
### What is it?
It is a tool that can count the characters, words, sentences, syllables and difficult words to calculate the [readability](https://en.wikipedia.org/wiki/Readability) of the given English text. Readability of a text can be found in multiple ways, including some simple and advanced formulas or methods. This tool uses 3 simple readability formulas, which are:

* [Automated Readability Index (ARI)](https://en.wikipedia.org/wiki/Automated_readability_index), uses the following formula to find the readability of a text:
```math
4.71 \cdot \Big( \frac{\#characters}{\#words} \Big) + 0.5 \cdot \Big( \frac{\#words}{\#sentences} \Big) - 21.43
```

* [Flesch–Kincaid Grade Level Test](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests), uses the following formula to find the readability of a text:
```math
0.39 \cdot \Big( \frac{\#words}{\#sentences} \Big) + 11.8 \cdot \Big( \frac{\#syllables}{\#words} \Big) - 15.59
```

* [Dale–Chall Readability Test](https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula), uses the following formula to find the readability of a text:
```math
0.1579 \cdot \Big( \frac{\#difficult \: words}{\#words} \cdot 100 \Big) + 0.0496 \cdot \Big( \frac{\#words}{\#sentences} \Big)
```
where the difficult words are all words that are not in the `frequents.txt`. If the percentage of the number of difficult words is above 5%, then we add +3.6365 to the raw score.

It is important to mention that due to the simplicity of these tests, the results can be highly misleading. In order to get a meaningful statistical result, one can try to increase the word count of the given text.

### How to Use
To use the tool, you will need a `.txt` file, say `foo.txt`, in the same directory where you will copy paste the text you want to analyze. For instance, let's say we have the following [text](https://en.wikipedia.org/wiki/Georg_Cantor#Mathematical_work) in `foo.txt`:

```
Cantor's work between 1874 and 1884 is the origin of set theory. Prior to this work, the concept of
a set was a rather elementary one that had been used implicitly since the beginning of mathematics,
dating back to the ideas of Aristotle. No one had realized that set theory had any nontrivial content.
Before Cantor, there were only finite sets (which are easy to understand) and "the infinite" (which
was considered a topic for philosophical, rather than mathematical, discussion). By proving that there
are (infinitely) many possible sizes for infinite sets, Cantor established that set theory was not
trivial, and it needed to be studied. Set theory has come to play the role of a foundational theory in
modern mathematics, in the sense that it interprets propositions about mathematical objects (for example,
numbers and functions) from all the traditional areas of mathematics (such as algebra, analysis, and
topology) in a single theory, and provides a standard set of axioms to prove or disprove them. The basic
concepts of set theory are now used throughout mathematics.
```

While in the `hyperskill-projects` directory with your text file `foo.txt`, run the following commands to use the tool:
```
cd readability
```
```
python readability.py foo.txt
```
Then, the results will show up:

```
Text: Cantor's work between 1874 and 1884 is the origin of set theory. Prior to this work, the concept of
a set was a rather elementary one that had been used implicitly since the beginning of mathematics,
dating back to the ideas of Aristotle. No one had realized that set theory had any nontrivial content.
Before Cantor, there were only finite sets (which are easy to understand) and "the infinite" (which
was considered a topic for philosophical, rather than mathematical, discussion). By proving that there
are (infinitely) many possible sizes for infinite sets, Cantor established that set theory was not
trivial, and it needed to be studied. Set theory has come to play the role of a foundational theory in
modern mathematics, in the sense that it interprets propositions about mathematical objects (for example,
numbers and functions) from all the traditional areas of mathematics (such as algebra, analysis, and
topology) in a single theory, and provides a standard set of axioms to prove or disprove them. The basic
concepts of set theory are now used throughout mathematics.

Characters: 904
Sentences: 7
Words: 176
Difficult words: 67
Syllables: 293


---- TEST RESULTS ----

Automated Readability Index: 14. The text can be understood by 18-22 year olds.
Flesch-Kincaid Readability Test: 14. The text can be understood by 18-22 year olds.
Dale-Chall Readability Index: 14. The text can be understood by 18-22 year olds.
This text should be understood in average by 20.0 year olds.
```
