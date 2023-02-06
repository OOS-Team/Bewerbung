# Bewerbung
Auflistung von Python und R Scripten aus Uni und Privatem.


## Python

- stimmungsanalyseVonBewertungen
>Dies ist ein Code in Python, der eine Stimmungsanalyse für die ersten 10.000 Amazon-Rezensionen von Kaggle durchführt. Der Code lädt die Rezensionen zunächst in einen Pandas-Datenrahmen und extrahiert den Rezensionstext daraus. >Dann wird das Natural Language Toolkit (NLTK) verwendet, um die Bewertungen in Sätze und Wörter zu tokenisieren und Adjektive aus den Sätzen zu extrahieren.> Die daraus resultierende Liste von Adjektiven wird zu einer Zeichenkette zusammengefügt, die als Merkmalssatz für die Stimmungsanalyse verwendet wird.

>Der Code verwendet dann die scikit-learn-Bibliothek, um die Merkmalsmenge und die Zielvariable (eine binäre Punktzahl, die angibt, ob die Bewertung positiv oder negativ ist) in Trainings- und Testmengen aufzuteilen. Die Merkmalsmenge wird mit Hilfe eines CountVectorizers, der die Anzahl der Vorkommen jedes Adjektivs in jeder Rezension zählt, in eine Dokument-Term-Matrix umgewandelt.

>Schließlich trainiert der Code einen Multinomial-Naive-Bayes-Klassifikator auf den Trainingsdaten und bewertet seine Leistung auf den Testdaten anhand der Genauigkeitsbewertung. Der Code gibt auch die prädiktivsten Adjektive aus, geordnet nach ihren Koeffizienten im Klassifikator.


## R

- sterberateCovid 
> In diesem Code werden einige Daten für COVID-19 geladen und vorbereitet. Danach werden drei verschiedene Modelle erstellt und trainiert, um das Sterberisiko von COVID-19-Patienten zu prognostizieren.

>Das erste Modell ist ein einfaches Modell mit festen Multiplikatoren, die von der Altersgruppe abhängen. Dieses Modell wird mit der Library DALEX gewrappt, um es zu visualisieren und zu analysieren.

>Das zweite Modell ist ein Entscheidungsbaum, der mit der Library partykit trainiert wurde. Auch dieser wird mit DALEX gewrappt.

>Das dritte Modell ist ein Random Forest-Modell, das mit mlr3 erstellt und trainiert wurde. Es wird ebenfalls mit DALEX gewrappt.

>Zum Schluss wird eine Hyperparameter-Optimierung mit mlr3tuning und paradox durchgeführt, um das Random Forest-Modell weiter zu verbessern.
