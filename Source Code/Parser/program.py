import utils as u
from taggers import tagger_sync, tagger_async
from tokenizers import tokenize, stem, lematizer
from anaphora_resolution import solve_anaphora_resolution

def apply_parser(text):
    anaphora_data = solve_anaphora_resolution("text", "ro")
    sents = tokenize(text)
    result = []
    for sent in sents:
        result.append(tagger_sync(sent))
    # tagger_async(document, 8)
    return result

if __name__ == '__main__':
    data, document = u.read_document()
    print(apply_parser(document))
