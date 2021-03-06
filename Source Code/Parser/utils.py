import sys, os

try:
    from html import unescape  # python 3.4+
except ImportError:
    try:
        from html.parser import HTMLParser  # python 3.x (<3.4)
    except ImportError:
        from HTMLParser import HTMLParser  # python 2.x
    unescape = HTMLParser().unescape

try:
    from html import escape  # python 3.x
except ImportError:
    from cgi import escape  # python 2.x

def read_document(file_name="Document.txt"):
    str = ""
    lis = []
    with open(file_name, 'r') as f:
        content = f.readlines()
    for cont in content:
        if (len(cont) == 1):
            lis.append(0)
        else:
            lis.append(len(cont))
        str += cont.replace('\n', ' ')
    str.replace('\n', ' ')
    return lis, str


def get_result(server_response):
    result = \
        str(server_response.content.decode(server_response.apparent_encoding)).split("<return>")[1].split("</return>")[
            0]
    if result == "":
        result = "No result from server :("
    return unescape(result)


def validate_language(language):
    languages_supported = ['ro', "en", "bg", "de", "el", "pl"]
    if language not in languages_supported:
        message = "Language \"%(language)s\" is not supported." % {"language": language}
        raise Exception(message)


def block_print():
    sys.stdout = open(os.devnull, 'w')


def enable_print():
    sys.stdout = sys.__stdout__
