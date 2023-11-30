import _pickle

my_file = 'hello_out.dat'

with open(my_file, 'rb') as f:
    lang_list = _pickle.load(f)
    print(lang_list)
    print(lang_list[2][0])
