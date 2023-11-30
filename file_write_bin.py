import _pickle

print('----------------------')
lang = ['Python', 'Java', 'C++']
vers = [3.11, 17, 14]

lang_vers = list(zip(lang, vers))
print(lang_vers)

my_file = 'hello_out.dat'
#with open(my_file, 'a') as f:
# 'wb' - write binary
with open(my_file, 'wb') as f:
    _pickle.dump(lang_vers, f)