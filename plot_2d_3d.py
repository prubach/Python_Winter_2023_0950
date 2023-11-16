list_of_points = [(1, 2), (3, 2), (-1, 3)]

import matplotlib.pyplot as plt

xs = [i[0] for i in list_of_points]
ys = [i[1] for i in list_of_points]

plt.plot(xs, ys, 'o')
plt.show()


list_of_points_3D = [[1, 2, 6], [3, 2, 3], [4, 3, 7]]

xs = [i[0] for i in list_of_points_3D]
ys = [i[1] for i in list_of_points_3D]
zs = [i[2] for i in list_of_points_3D]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(xs, ys, zs, marker='^')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

