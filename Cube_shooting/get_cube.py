#!/usr/bin/python
# -*- coding: GBK -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib
# 使用TkAgg作为Matplotlib的后端，以支持交互式绘图
matplotlib.use('TkAgg')

# 定义八个顶点的坐标
vertices = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
    [1, 0, 1]
])

# 定义六个面
faces = np.array([
    [0, 1, 2, 3],  # 底部
    [4, 5, 6, 7],  # 顶部
    [0, 1, 5, 4],  # 左侧
    [2, 3, 7, 6],  # 右侧
    [1, 2, 6, 5],  # 正面
    [0, 3, 7, 4]   # 背面
])

# 定义每个顶点的颜色
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'orange', 'purple']

# 创建一个3D坐标系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制立方体的每个面，并设置每个面的颜色
# for i, face in enumerate(faces):
#     collection = Poly3DCollection([vertices[face]], alpha=0.25, facecolor=colors[i])
#     ax.add_collection(collection)

# 绘制每个顶点，并设置颜色
for i, vertex in enumerate(vertices):
    ax.scatter(vertex[0], vertex[1], vertex[2], c=colors[i])

# 设置坐标轴范围
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# 设置初始视角
ax.view_init(elev=0, azim=0)

# 显示图形
plt.show()