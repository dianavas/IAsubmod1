from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer,SnowballStemmer
import utils as u
import re
import time
JOBSCOUNT = 8

data, document = u.read_document()

# exemplu de cum sa cauti ce inseamna un anumit tagset
# import nltk
# nltk.help.upenn_tagset('POS')

# http://snowball.tartarus.org/algorithms/romanian/stemmer.html
# stemmer

def stem_word(word):
    lancaster_stemmmer = SnowballStemmer("romanian")
    return lancaster_stemmmer.stem(word)

def lematizer_word(word):
    wordnet_lemmatizer = WordNetLemmatizer()
    return wordnet_lemmatizer.lemmatize(word)

# tagger sync
def tagger_sync(data):
    start = time.time()
    import treetaggerwrapper
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='ro')
    tags = tagger.tag_text(data)

    # [(cuvant, clasificare, lemma)]
    result = []
    for tag in tags:
        dt = re.split(r'\t+', tag)
        t = {"word":dt[0], "pos":dt[1], "lemma":dt[2]}
        result.append(t)
    print("Finished after {:0.2f} seconds elapsed".format(time.time() - start))
    return result

def tagger_async(data, n = None):
    start = time.time()
    import treetaggerpoll

    # Note: print() have been commented, you may uncomment them to see progress.
    p = treetaggerpoll.TaggerProcessPoll(workerscount=n,TAGLANG="ro")
    res = []

    chunk_len = len(data)//JOBSCOUNT
    chuncks = [data[i:i+chunk_len] for i in range(0, len(data), chunk_len)]

    print("Creating jobs")
    for i in range(JOBSCOUNT):
        res.append(p.tag_text_async(chuncks[i]))

    print("Waiting for jobs to complete")
    for i, r in enumerate(res):
        r.wait_finished()

    p.stop_poll()
    print("Finished after {:0.2f} seconds elapsed".format(time.time() - start))

if __name__ == '__main__':
    print(tagger_sync(document))
    # tagger_async(document, 8)