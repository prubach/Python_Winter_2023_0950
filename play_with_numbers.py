num_list = [2, 13, 9, 7, 11, 5, 18, 7, 9]

'''
TODO 
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''
num_list_2nd_pow = [x*x for x in num_list]
print(num_list_2nd_pow)
num_list_2nd_pow_sorted = sorted(num_list_2nd_pow)
num_list_2nd_pow_sorted = sorted(num_list_2nd_pow, reverse=True)
print(num_list_2nd_pow_sorted)
#sum(num_list_2nd_pow)
print('------ set --------')
set_of_nums = set(num_list_2nd_pow_sorted)
print(set_of_nums)
print('------ tuples --------')
t = (10, 57, 37)
x, y, z = t
print(x, y, z)
print(t)
for i in t:
    print(i)
print('------ tuples 2D --------')
list_of_points = [(1, 2), (3, 2), (-1, 3)]
for x, y in list_of_points:
    print(f'x={x}, y={y}')

print('------ matrix --------')
list_of_points_3D = [[1, 2, 6], [3, 2, 3], [4, 3, 7]]
#print(list_of_points_3D)

import matplotlib.pyplot as plt
import numpy as np


all_points = np.array(list_of_points_3D)
x = [i[0] for i in list_of_points]
y = [i[1] for i in list_of_points]
#z = [i[2] for i in all_points]
#xpoints = np.array([1, 8])
#ypoints = np.array([3, 10])

plt.plot(x, y, 'o')
plt.show()


xs = [i[0] for i in list_of_points_3D]
ys = [i[1] for i in list_of_points_3D]
zs = [i[2] for i in list_of_points_3D]


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(xs, ys, zs, marker='^')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

for row in list_of_points_3D:
    print(row)

# TODO:
# 1. Print the sum of each row
row_sums = []
for row in list_of_points_3D:
    row_sum = sum(row)
    row_sums.append(row_sum)
    print(f"{'The sum of the row'} {row}:{row_sum}")
print(row_sums)
# 2. Print the sum of each column
col_sums = [0, 0, 0]
for row in list_of_points_3D:
    for i in range(len(row)):
         col_sums[i] += row[i]
print(col_sums)

col_sum = [0, 0, 0]
for row in list_of_points_3D:
    print(row)
    for i in range(len(row)):
        col_sum[i] += row[i]

print(col_sum)


languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]
result = zip(languages, versions)

print(list(result))

res = [sum(idx) for idx in zip(*list_of_points_3D)]
print(res)



# 3. Print the sum of all elements
print(sum(row_sums))

print('----------------------')
lang = ['Python', 'Java', 'C++']
vers = [3.11, 17, 14]

lang_vers = list(zip(lang, vers))
print(lang_vers)

print('----Sum of cols using zip ------------------')
col_sums = [sum(els) for els in zip(*list_of_points_3D)]
print(col_sums)

