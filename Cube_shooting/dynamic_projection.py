#!/usr/bin/python
# -*- coding: GBK -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'orange', 'purple']

radius = 10
center = np.array([0, 0, 0])
theta = np.linspace(0, 2 * np.pi, 36)
x = radius * np.cos(theta)
z = radius * np.sin(theta)
t = np.vstack((x, np.zeros_like(x), z)).T
t = np.vstack((t[9:, :], t[:9, :]))
t = np.flip(t, axis=0)
# 定义相机内参
K = np.array([[1000, 0, 500], [0, 1000, 500], [0, 0, 1]])

# 初始化相机位姿
# R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 旋转矩阵
# T = np.array([[0, 0, -10]]).T  # 平移向量

# # 创建一个3D坐标系
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # 绘制立方体的每个面
# faces = [[0,1,2,3], [0,1,5,4], [1,2,6,5], [2,3,7,6], [3,0,4,7], [4,5,6,7]]
# colors = ['r', 'g', 'b', 'c', 'm', 'y']
# for i in range(6):
#     collection = Poly3DCollection([vertices[faces[i]]], alpha=0.25, facecolor=colors[i])
#     ax.add_collection3d(collection)

fig, ax = plt.subplots()
# # 投影顶点到相机平面
# projected_vertices = np.dot(K, np.dot(R, vertices.T) + T)
# projected_vertices = np.divide(projected_vertices, projected_vertices[2, :], casting="unsafe")
#
# 绘制投影点
# ax.scatter(projected_vertices[0], projected_vertices[1], s=50)
i = 0
# 围绕立方体旋转相机
for angle in range(0, 360, 10):
    # 计算旋转矩阵
    R = np.array([[np.cos(np.radians(angle)), 0, np.sin(np.radians(angle))],
                  [0, 1, 0],
                  [-np.sin(np.radians(angle)), 0, np.cos(np.radians(angle))]])

    # 更新相机位姿
    T = np.array([[0, 0, -10]]).T  # 平移向量
    # T = np.array([t[i]]).T
    # i = i + 1
    RT = np.hstack((R, T))
    P = np.dot(K, np.dot(RT, np.vstack((vertices.T, np.ones((1, 8))))))  # 投影矩阵

    # 绘制投影点
    projected_vertices = P / P[2, :]
    ax.scatter(projected_vertices[0], projected_vertices[1], c=colors, s=50)

    # 设置坐标轴范围
    ax.set_xlim([0, 1000])
    ax.set_ylim([0, 1000])


    # 显示图形
    plt.show(block=False)
    plt.pause(1)
    ax.cla()