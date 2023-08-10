import numpy as np
import struct
import os
import sys
import open3d as o3d


def bin_to_pcd(binFileName):
    size_float = 4
    list_pcd = []
    with open(binFileName, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_pcd)
    return pcd


def main(binFolderName, pcdFolderName):
    sortedBinFileNames = os.listdir(binFolderName)
    sortedBinFileNames.sort()
    for i in sortedBinFileNames:
        if not i.startswith('.'):
            binFileName = binFolderName + '/' + i
            print(i)

            pcd = bin_to_pcd(binFileName)
            pcdFileName = pcdFolderName+i[:-4]+'.pcd'
            print(pcdFileName)
            o3d.io.write_point_cloud(pcdFileName, pcd)


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    main(a, b)
