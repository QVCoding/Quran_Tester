# Quran Tester
HTML-based Quran (Hifdh) testing apps.

Are made public on [https://qurantester.neocities.org](https://qurantester.neocities.org)

# Files
All Quranic data is taken from [tanzil.org](https://tanzil.net/docs/).

`app_quran_metadata.xml` Quranic metadata taken from [https://tanzil.net/docs/quran_metadata](https://tanzil.net/docs/quran_metadata), modified to include only surah, juz, and page.

`quran_words.csv` List of every word in the Quran. 

How to reproduce:
From [https://tanzil.net/download/](https://tanzil.net/download/) download the `Simple (Plain)` SQL text, with all options disabled.
Run `make_quran_words.py`, then convert the resulting file to csv.

 `Minimum_Phrase_Tester.html` App which shows a unique-phrase (with no more words than necessary for the phrase to be uniquely identifiable) for the user to identify.

 `Occurrences_Tester.html` App which tests the user in identifying the recurrences of phrases in the Quran.
