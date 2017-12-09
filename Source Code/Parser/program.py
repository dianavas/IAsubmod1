from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import utils as u

data, document = u.read_document()
words = word_tokenize(document)
phrases = sent_tokenize(document)

print(words, phrases)

# word tokenize folosing limba romana
print(pos_tag(word_tokenize(document), tagset='universal', lang='ro'))

# exemplu de cum sa cauti ce inseamna un anumit tagset
import nltk
nltk.help.upenn_tagset('POS')

#stemmer

# http://snowball.tartarus.org/algorithms/romanian/stemmer.html
from nltk.stem import SnowballStemmer
lancaster_stemmmer = SnowballStemmer("romanian")
print(lancaster_stemmmer.stem("abruptă"))

# lematizer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize("churches"))
# pentru romana e cu ?