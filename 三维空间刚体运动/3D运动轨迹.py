import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建Matplotlib 3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 假设机器人的位置信息保存在一个列表中，每个元素为一个三元组(x, y, z)
robot_poses = [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]

# 绘制机器人的运动轨迹
x = [p[0] for p in robot_poses]
y = [p[1] for p in robot_poses]
z = [p[2] for p in robot_poses]
ax.plot(x, y, z, '-o')

# 设置坐标轴标签和标题
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('SLAM Trajectory')

# 显示Matplotlib 3D图形
plt.show()