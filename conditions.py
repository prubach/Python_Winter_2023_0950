p = True
q = True

if p:
    print('p is True')
    #print('p is True')
else:
    print('p is False')

if not p:
    print('not p True')
else:
    print('not p False')

if p and q:
    print('p and q True')
else:
    print('p and q False')

if p or q:
    print('p or q True')
else:
    print('p or q False')

# XOR
if p ^ q:
    print('p xor q True')
else:
    print('p xor q False')

print('----------------')

a = 10
if a >= 12:
    print('a>=12')
else:
    print('a<12')

s1 = 'abc'
s2 = 'absgwc'

if s1 == s2:
    print('s1 = s2')
else:
    print('s1 != s2')

y = 10 if s1 == s2 else 32
print(y)