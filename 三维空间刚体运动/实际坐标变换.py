import numpy as np
import quaternion


def transT(R, t):
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    # M = np.dot(T, np.hstack((R, np.zeros((3, 1)))))
    T[3, :3] = 0
    T[3, 3] = 1
    return T
t1 = np.array([0.3, 0.1, 0.1])
q1 = np.quaternion(0.35, 0.2, 0.3, 0.1)
t2 = np.array([-0.1, 0.5, 0.3])
q2 = np.quaternion(-0.5, 0.4, -0.1, 0.2)
# 将四元数和平移向量组合成变换矩阵
R1 = quaternion.as_rotation_matrix(q1)
R2 = quaternion.as_rotation_matrix(q2)
T1 = transT(R1, t1)
T2 = transT(R2, t2)
v = np.array([0.5, 0, 0.2, 1])

# 进行变换
v_new = np.dot(np.linalg.inv(T1), v)
v_new = np.dot(T2, v_new)

# 输出变换前后的向量
print("变换前的向量：", v[:3])
print("变换后的向量：", v_new[:3])