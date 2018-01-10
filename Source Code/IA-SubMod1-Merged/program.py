import os
from parser_v1 import parse
from files_reader import ConvertData, ConvertFile

input_file_path = "c:\\Users\\Turcu Nicusor\\Desktop\\Work\\Anul 3\\IA\\Project\\Source Code\\IA-SubMod1-Merged\\test\\"
output_file_path ="c:\\Users\\Turcu Nicusor\\Desktop\\Work\\Anul 3\\IA\\Project\\Source Code\\IA-SubMod1-Merged\\test\\xml_files"

# to add cleanup function
ConvertFile(input_file_path)
# to fix marked errors
parse(input_file_path=os.path.join(input_file_path, "text_files"), output_file_path=output_file_path)
