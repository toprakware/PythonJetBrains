# Multilingual Translator
### What is it?

This tool is a simple multilingual translator that supports 13 different languages. Although it can only translate words,
it also gives some example sentences containing the translated word.

This tool uses [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/) to parse the translation data from the https://context.reverso.net/translation/ website.

### How to Use
To use the tool, while in the `hyperskill-projects` directory, run the following commands:
```
cd translator
```
```
python translator.py [source] [target] [word]
```

where `source` is the language the `word` was written in, `target` is the language you want the `word` to be translated and
`word` is the word you want to translate.

For instance, for source = english, target = turkish, and word = mathematics; we have:
```
python translator.py english turkish mathematics
```
```
Turkish Translations:
matematik
uzbilim
matematiksel

Turkish Examples:
Both aspects are as old as the science of mathematics itself.
Her iki bakış açısı da matematik bilimi kadar eskidir.

As though poetry were a science; or mathematics an art.
Sanki şiir bilimmiş, matematik de bir sanatmış gibi.
```

As an extra feature, it is possible to use the `all` keyword for the target option to translate the given word in source
language to all 12 remaining languages:
```
Arabic Translations:
رياضيات
حساب
رياضة

Arabic Examples:
Gerolamo Cardano, a pioneer on the mathematics of probability.
جيرولامو كاردانو، من بين أقدم رواد رياضيات الاحتمالات.

I credit my mother with much of my success in mathematics.
الاول الائتمان امي بلادي مع الكثير من النجاح في الرياضيات.


German Translations:
Mathematik
Mathe
Mathematiker

German Examples:
There is no permanent place in the world for ugly mathematics.
Es gibt keinen festen Platz in der Welt für hässliche Mathematik.

He transformed the subject into a rich domain of modern mathematics.
Er verwandelte das Thema in eine reiche Domäne der modernen Mathematik.


Spanish Translations:
matemático
matemática
Mathematics

Spanish Examples:
His scientific interests led him to publish on physics and mathematics.
Sus intereses científicos lo llevan a publicar en física y en matemáticas.

James learnt mathematics first from his mother who taught him geometry.
James aprendió matemáticas de primero a su madre que le enseñó geometría.


French Translations:
mathématique
maths
mathématiciens

French Examples:
I had a very scientific education: mathematics, artificial intelligence.
Mon éducation a été très scientifique, mathématique, intelligence artificielle.

Introduction to axiomatic set theory and to the encoding of mathematics.
Introduction à la théorie axiomatique des ensembles et au codage mathématique.


Hebrew Translations:
מתמטיקה
מתימטיקה
מתמטי

Hebrew Examples:
Most students have no idea why they have to study mathematics.
רוב התלמידים לא מבינים מדוע הם צריכים ללמוד כלל מתמטיקה.

The main task is to develop new programs using mathematics.
המשימה העיקרית היא לפתח תוכניות חדשות באמצעות מתמטיקה.


Japanese Translations:
数学
数理
算数

Japanese Examples:
She excelled in astronomy and mathematics.
彼女は天文学と数学において卓越していた。

He showed exceptional ability in mathematics.
彼は数学に優れた能力を示した。


Dutch Translations:
wiskunde
wiskundige
mathematica

Dutch Examples:
Early testing indicated high predisposition... towards science and mathematics.
Vroege tests wezen op een grote aanleg... voor natuur- en wiskunde.

I believe they shared a mathematics tutor.
Ik geloof dat ze samen dezelfde wiskunde leraar hadden.


Polish Translations:
matematyka
matematyczny
matematyków

Polish Examples:
Leonardo received an informal education in Latin, geometry and mathematics.
Leonardo otrzymał nieformalne wykształcenie w takich dziedzinach jak język łaciński, geometria i matematyka.

Novica, mathematics is... like music.
Novica, matematyka jest jak... jak muzyka.


Portuguese Translations:
matemática
Mathematics
matemático

Portuguese Examples:
Not magic gas head, mathematics.
Nada de magia, cabeça de gás, matemática.

This theorem also has important roles in constructive mathematics and proof theory.
Tal teorema também desempenha papeis importantes na matemática construtiva e na teoria da prova.


Romanian Translations:
matematică
matematic
matematice

Romanian Examples:
But the whole system is irrelevant after dialectical mathematics.
Dar întregul sistem este lipsit de relevanță, după matematica dialectice.

With mathematics we may soon understand them.
Cu matematica am putea în curând să le înțelegem.


Russian Translations:
математик
математика
математический

Russian Examples:
In mathematics, where proofs are everything.
В математике, где доказательство - это всё, важны также и факты.

My interest in mathematics developed later.
Мой интерес к математике - это то. что развилось позднее.


Turkish Translations:
matematik
uzbilim
matematiksel

Turkish Examples:
Both aspects are as old as the science of mathematics itself.
Her iki bakış açısı da matematik bilimi kadar eskidir.

As though poetry were a science; or mathematics an art.
Sanki şiir bilimmiş, matematik de bir sanatmış gibi.
```
