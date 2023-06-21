#!/usr/bin/python
# -*- coding: GBK -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib
# ʹ��TkAgg��ΪMatplotlib�ĺ�ˣ���֧�ֽ���ʽ��ͼ
matplotlib.use('TkAgg')

# ����˸����������
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

# ����������
faces = np.array([
    [0, 1, 2, 3],  # �ײ�
    [4, 5, 6, 7],  # ����
    [0, 1, 5, 4],  # ���
    [2, 3, 7, 6],  # �Ҳ�
    [1, 2, 6, 5],  # ����
    [0, 3, 7, 4]   # ����
])

# ����ÿ���������ɫ
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'orange', 'purple']

# ����һ��3D����ϵ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# �����������ÿ���棬������ÿ�������ɫ
# for i, face in enumerate(faces):
#     collection = Poly3DCollection([vertices[face]], alpha=0.25, facecolor=colors[i])
#     ax.add_collection(collection)

# ����ÿ�����㣬��������ɫ
for i, vertex in enumerate(vertices):
    ax.scatter(vertex[0], vertex[1], vertex[2], c=colors[i])

# ���������᷶Χ
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# ���ó�ʼ�ӽ�
ax.view_init(elev=0, azim=0)

# ��ʾͼ��
plt.show()