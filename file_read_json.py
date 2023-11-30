import json

my_file = 'hello_out.json'

with open(my_file, 'r') as f:
    lang_list = json.load(f)
    print(lang_list)
    print(lang_list[2][0])
