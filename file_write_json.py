import json

print('----------------------')
lang = ['Python', 'Java', 'C++']
vers = [3.11, 17, 14]

lang_vers = list(zip(lang, vers))
print(lang_vers)

my_file = 'hello_out.json'
#with open(my_file, 'a') as f:
# 'w' - write text
with open(my_file, 'w') as f:
    json.dump(lang_vers, f)