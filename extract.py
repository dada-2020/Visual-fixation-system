import cv2
import os

def extract(string video_path, int frameFrequency)
    times=0
    #输出图片到当前目录vedio文件夹下
    outPutDirName='vedio/'+sourceFileName+'/'
    if not os.path.exists(outPutDirName):
    #如果文件目录不存在则创建目录
    os.makedirs(outPutDirName) 
    camera = cv2.VideoCapture(video_path)
    while True:
        times+=1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            break
        if times%frameFrequency==0:
            cv2.imwrite(outPutDirName + str(times)+'.jpg', image)
            print(outPutDirName + str(times)+'.jpg')
    print('图片提取结束')
    camera.release()