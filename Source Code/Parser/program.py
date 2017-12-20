import utils as u
# from taggers import tagger_sync, tagger_async
# from tokenizers import tokenize, stem, lematizer
import pos_tagger, np_chuncker, fdg_parser_ro, anaphora_resolution


# def apply_parser_v1(document):
#     sents = tokenize(document)
#     result = []
#     for sent in sents:
#         result.append(tagger_sync(sent))
#     # tagger_async(document, 8)
#     return result

def apply_parser_v2(document):
    data = fdg_parser_ro.parse_text(document)
    return anaphora_resolution.solve_links_manual(data)

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    data, document = u.read_document()
    print(apply_parser_v2(document))

