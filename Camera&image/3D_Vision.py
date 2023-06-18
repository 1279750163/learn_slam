import cv2
import numpy as np
import open3d as o3d
import time

class point_cloud_generator():
    def __init__(self, bgr_file, depth_file, save_ply, camera_intrinsics=[784.0, 779.0, 649.0, 405.0]):
        self.bgr_file = bgr_file
        self.depth_file = depth_file
        self.save_ply = save_ply

        self.bgr = cv2.imread(self.bgr_file)
        self.rbg = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2RGB)
        self.depth = cv2.imread(self.depth_file, -1)
        self.depth = self.depth.astype(np.float64)
        print('your depth image shape is:', self.depth.shape)

        self.width = self.rbg.shape[1]
        self.height = self.rbg.shape[0]
        self.camera_intrinsics = camera_intrinsics


    def trans(self, X, Y, SFz = 0.0005 , SFx = 0.0196, SFy = 0.0196):
        self.Z = (self.depth - 32768) * SFz
        self.X = X * SFx
        self.Y = Y * SFy

    def compute(self):
        t1 = time.time()
        X = np.zeros((self.width, self.height))
        Y = np.zeros((self.width, self.height))
        for i in range(self.height):
            X[i, :] = np.full(X.shape[1], i)

        for i in range(self.width):
            Y[:, i] = np.full(Y.shape[0], i)

        self.trans(X, Y)
        data_ply = np.zeros((6, self.width * self.height))
        data_ply[0] = self.X.T.reshape(-1)
        data_ply[1] = -self.Y.T.reshape(-1)
        data_ply[2] = self.Z.reshape(-1)
        img = np.array(self.rbg, dtype=np.uint8)
        data_ply[3] = img[:, :, 0:1].reshape(-1)
        data_ply[4] = img[:, :, 1:2].reshape(-1)
        data_ply[5] = img[:, :, 2:3].reshape(-1)
        self.data_ply = data_ply
        t2 = time.time()
        print('calcualte 3d point cloud Done.', t2 - t1)

    def write_ply(self):
        start = time.time()
        float_formatter = lambda x: '%.4f' % x
        points = []
        for i in self.data_ply.T:
            points.append('{} {} {} {} {} {} 0\n'.format(
                float_formatter(i[0]), float_formatter(i[1]), float_formatter(i[2]),
                int(i[3]), int(i[4]), int(i[5])
            ))

        file = open(self.save_ply, 'w')
        file.write('''ply
                        format ascii 1.0
                        element vertex %d
                        property float x
                        property float y
                        property float z
                        property uchar red
                        property uchar green
                        property uchar blue
                        property uchar alpha
                        end_header
                        %s
                        ''' % (len(points), "".join(points)))
        file.close()

        end = time.time()
        print("Write into .ply file Done.", end - start)

    def show_point_cloud(self):
        pcd = o3d.io.read_point_cloud(self.save_ply)
        o3d.visualization.draw([pcd])

if __name__ == '__main__':
    camera_intrinsics = [378.998657, 378.639862, 321.935120, 240.766663]
    rgb_file = '../img/img01_Color.png'
    depth_file = '../img/img01_3D.png'
    save_file = '../ply/img01.ply'
    a = point_cloud_generator(rgb_file, depth_file, save_file, camera_intrinsics)

    a.compute()
    a.write_ply()
    a.show_point_cloud()