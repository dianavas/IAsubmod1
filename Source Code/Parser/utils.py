def read_document(file_name="Document.txt"):
    str = ""
    lis = []
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.readlines()
    for cont in content:
        if (len(cont) == 1):
            lis.append(0)
        else:
            lis.append(len(cont))
        str += cont.replace('\n', ' ')
    str.replace('\n', ' ')
    return lis, str
