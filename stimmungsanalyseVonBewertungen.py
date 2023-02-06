# Importiere notwendige Bibliotheken
import pandas as pd
import nltk

# Lade Daten
df = pd.read_csv("./Reviews_10000.csv.bz2")

# Extrahiere Texte aus dem Datensatz
texts = df["Text"]

# Lade den "averaged perceptron tagger" aus NLTK
nltk.download('averaged_perceptron_tagger')

# Transformiere die Texte in eine Liste von adjektivbehafteten Wörtern
texts_transformed = []
for review in texts: 
    # Zerteile den Text in Sätze
    sentences = nltk.sent_tokenize(review)
    adjectives = []
    
    # Zerteile jeden Satz in Wörter
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        
        # Verwende den "averaged perceptron tagger", um Part-of-Speech-Tags für jedes Wort zu generieren
        words_tagged = nltk.pos_tag(words)
        
        # Filtere die Adjektive aus den Wörtern heraus
        for word_tagged in words_tagged:
            if word_tagged[1] == "JJ":
                adjectives.append(word_tagged[0])
                
    # Verbinde die Adjektive zu einem Text
    texts_transformed.append(" ".join(adjectives))

# Verwende die transformierten Texte als Daten (X) und Bewertungen als Ziel (y)
X = texts_transformed
y = df["Score"] >= 4

# Teile die Daten in Trainings- und Testdaten auf
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)

# Verwende die "CountVectorizer" aus scikit-learn, um die Daten in eine numerische Form zu bringen
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 50)
cv.fit(X_train)
X_train = cv.transform(X_train)
X_test = cv.transform(X_test)

# Trainiere ein Modell auf den Trainingsdaten
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB() # Multinomialer Naive Bayes für Textklassifikation
model.fit(X_train, y_train)

# Berechne die Genauigkeit des Modells auf den Testdaten
print(model.score(X_test, y_test))

# Zeige die 50 wichtigsten Adjektive und deren Gewichtungen im Modell an
adj = list(zip(model.coef_[0], cv.get_feature_names()))
adj = sorted(adj)
for i in adj:
   print(i)
