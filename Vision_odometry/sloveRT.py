import cv2
import numpy as np


def get_points(pointfile):
    matches = np.loadtxt(pointfile)
    point01 = matches[:, :2]
    point02 = matches[:, 2: 4]
    return point01, point02
def get_fundamental_matrix(points1, points2):
    fundamental_matrix, _ = cv2.findFundamentalMat(points1, points2, method=cv2.FM_8POINT)
    return fundamental_matrix

def get_essential_matrix(points1, points2, cameraMatrix):
    essential_matrix, _ = cv2.findEssentialMat(points1, points2, cameraMatrix, cv2.RANSAC)
    return essential_matrix

def get_R_T(essential_matrix, points1, points2):
    _, R, T, _ = cv2.recoverPose(essential_matrix, points1, points2)
    return R, T


if __name__ == '__main__':
    points1, points2 = get_points('../data_point/pointdata1_4_0.4.txt')
    fundamental_matrix = get_fundamental_matrix(points1, points2)