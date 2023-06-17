import numpy as np
import quaternion

q1 = np.quaternion(1,2,3,4)
q2 = quaternion.from_float_array([1,2,3,4])

# 生成的都是单位四元数
q3 = quaternion.from_rotation_matrix([[1,2,3],[1,2,3],[1,2,3]])
q4 = quaternion.from_euler_angles([1,2,3])
print(q1,q2,q3,q4)