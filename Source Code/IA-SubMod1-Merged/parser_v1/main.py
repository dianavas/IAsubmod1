import utils as u
import fdg_parser_ro, anaphora_resolution
import sys, os

# def apply_parser_v1(document):
#     sents = tokenize(document)
#     result = []
#     for sent in sents:
#         result.append(tagger_sync(sent))
#     # tagger_async(document, 8)
#     return result

def apply_parser(document):
    data = "default"
    try:
        data = fdg_parser_ro.parse_text(document)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error at calling fdg_parser. Reason:", str(e), "File:",fname , "Line:", exc_tb.tb_lineno)
    result = ""
    try:
        result = anaphora_resolution.solve_links_manual(data)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error at anaphora resolution. Reason:", str(e), "File:",fname , "Line:", exc_tb.tb_lineno)
    return result


def parse(input_file_path, output_file_path):
    files_info = u.read_from_path(input_file_path)
    for file_info in files_info:
        result = apply_parser(file_info["data"])
        u.write_xml(output_file_path, file_info["filename"], result)
