def compareFiles(file1_path, file2_path):
    file1 = open(file1_path, "r")
    file1_content = file1.read()

    file2 = open(file2_path, "r")
    file2_content = file2.read()

    if file1_content == file2_content:
        return True

    return False