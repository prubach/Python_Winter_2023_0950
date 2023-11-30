my_file = 'hello_out.txt'
#with open(my_file, 'a') as f:
# 'a' - append to file
# 'w' - overwrite file
with open(my_file, 'a') as f:
    f.write('1st line\n')
    f.write('2nd line\n')
    f.write('3rd line\n')
