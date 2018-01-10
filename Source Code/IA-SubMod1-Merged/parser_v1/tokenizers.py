from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer


# http://snowball.tartarus.org/algorithms/romanian/stemmer.html
# stemmer
def stem(word):
    lancaster_stemmmer = SnowballStemmer("romanian")
    return lancaster_stemmmer.stem(word)


def lematizer(word):
    wordnet_lemmatizer = WordNetLemmatizer()
    return wordnet_lemmatizer.lemmatize(word)


def tokenize(data):
    return sent_tokenize(data)
