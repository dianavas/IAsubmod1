import utils as u
from taggers import tagger_sync, tagger_async
from tokenizers import tokenize, stem, lematizer
import pos_tagger, np_chuncker, fdg_parser_ro, anaphora_resolution


def apply_parser(text):
    sents = tokenize(text)
    result = []
    for sent in sents:
        result.append(tagger_sync(sent))
    # tagger_async(document, 8)
    return result


if __name__ == '__main__':
    data, document = u.read_document()
    # print(apply_parser(document))
    # print(pos_tagger.parse_sentence_text("Ana are mere multe. Cate mere are ana?"))
    # print(anaphora_resolution.solve_links("Ana are mere multe. Cate mere are ana?", "ro"))
    # print(fdg_parser_ro.parse_text("Ana are mere multe. Cate mere are ana?"))
    #u.block_print()

    # print(pos_tagger.parse_text_text("Ana are mere multe"))
    print(np_chuncker.chunck_text("Ana are mere multe"))
    #u.enable_print()
