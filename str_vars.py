s = 'abcdefghij'
print(s)
print(len(s))
print(s[1:3])
print(s[3])
print(s[:3])
print(s[3:])
print('-----------------')
print('abc\nbcde')
print('1414\t251262\t14251\t51521')
s2 = '1414\t251262\t14251\t51521'
print(s2.split('\t'))
s3 = 'abc\nbcde'
print(s3.splitlines())

print("I can't")
print('Hello "Pawel"')
print('I can\'t')
print('anfagfa\\nskgshheh')
s4 = 'anghkgfagfa\\tgedgfvśśłłłąććąęęąęęwdg'
print(s4)
fa_count = s4.count('fa')
print(f'fa appears x times: {fa_count}')
# Throws ValueError if not found
fa_pos = s4.index('fa')
print(f'fa postion: {fa_pos}')

fa_pos = s4.rindex('fa')
print(f'fa reversed postion: {fa_pos}')

# Returns -1 if not found
fa_find = s4.find('fassd')
print(f'fa found: {fa_find}')

print(ord('a'))
print(ord('ł'))

s5 = '   ehehhweh wehewhew       '
print(s5)
print(s5.strip())
