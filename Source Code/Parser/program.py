from nltk.tokenize import sent_tokenize, word_tokenize
import utils as u

data, document = u.read_document()
words = word_tokenize(document)
phrases = sent_tokenize(document)

print(words, phrases)