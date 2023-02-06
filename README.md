# Bewerbung
Auflistung von Python und R Scripten aus Uni und Privatem.


## Python


## R

- sterberateCovid 
> In diesem Code werden einige Daten für COVID-19 geladen und vorbereitet. Danach werden drei verschiedene Modelle erstellt und trainiert, um das Sterberisiko von COVID-19-Patienten zu prognostizieren.

>Das erste Modell ist ein einfaches Modell mit festen Multiplikatoren, die von der Altersgruppe abhängen. Dieses Modell wird mit der Library DALEX gewrappt, um es zu visualisieren und zu analysieren.

>Das zweite Modell ist ein Entscheidungsbaum, der mit der Library partykit trainiert wurde. Auch dieser wird mit DALEX gewrappt.

>Das dritte Modell ist ein Random Forest-Modell, das mit mlr3 erstellt und trainiert wurde. Es wird ebenfalls mit DALEX gewrappt.

>Zum Schluss wird eine Hyperparameter-Optimierung mit mlr3tuning und paradox durchgeführt, um das Random Forest-Modell weiter zu verbessern.
