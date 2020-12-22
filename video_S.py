import socket
import threading
import struct
import time
import cv2
import numpy
#
# 服务器分析：
#
# 1.　先通过在服务器端利用OpenCV捕获到视频的每一帧图片
#
# 2.　将这些图片进行压缩成JPEG格式，这样能减小图片大小，便于传输
#
# 3.　按照提前协商好的分辨率和帧数进行打包编码传输
#
# 4.　利用服务器端打开端口8880，此时客户端连接后，便可以在客户端中捕获到服务器端的视频。



class Carame_Accept_Object:
    def __init__(self,S_addr_port=("",8880)):    #S_addr_port 是一个元组  ，self初始化对应的实例变量
        self.resolution=(640,480)       #执行该实例化的分辨率，self相当于int，定义的意思
        self.addr_port=S_addr_port      #地址绑定，addr_port 对应的端口号
        self.Set_Socket(self.addr_port)  #建立连接，调用一个函数

     #设置套接字
    def Set_Socket(self,S_addr_port):
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #选择TCP协议连接
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #端口可复用
        self.server.bind(S_addr_port)            #绑定端口号
        self.server.listen(5)                   #监听端口号
         #print("the process work in the port:%d" % S_addr_port[1])


def check_option(object,client):                  #按格式解码，确定帧数和分辨率，定义一个函数
     info=struct.unpack('lhh',client.recv(8))       #将接受到的传输帧数，分辨率解码
     if info[0]>888:                               #若第一个数值
        object.img_fps=int(info[0])-888            #获取帧数
        object.resolution=list(object.resolution)    # 获取分辨率
        object.resolution[0]=info[1]
        object.resolution[1]=info[2]
        object.resolution = tuple(object.resolution)
        return 1
     else:
        return 0

def RT_Image(object,client,D_addr):
     if(check_option(object,client)==0):
         return
     camera=cv2.VideoCapture(0)                                #从摄像头中获取视频
     img_param=[int(cv2.IMWRITE_JPEG_QUALITY),object.img_fps]  #设置传送图像格式、帧数
     while(1):
         time.sleep(0.1)                                       #推迟线程运行0.1s
         _,object.img=camera.read()                            #读取视频每一帧
         object.img=cv2.resize(object.img,object.resolution)     #按要求调整图像大小(resolution必须为元组)
         _,img_encode=cv2.imencode('.jpg',object.img,img_param)  #按格式生成图片
         img_code=numpy.array(img_encode)                        #转换成矩阵
         object.img_data=img_code.tostring()                     #生成相应的字符串
         try:
             client.send(struct.pack("lhh",len(object.img_data),object.resolution[0],object.resolution[1])+object.img_data)  #按照相应的格式进行打包发送图片 t图传指令
         except:
             camera.release()        #释放资源
             return

if __name__ == '__main__':
     camera=Carame_Accept_Object()             #执行这个类
     while(1):
         client,D_addr=camera.server.accept()    #服务器接受到来自客户端的连接，收到客户端的信息为
         clientThread=threading.Thread(None,target=RT_Image,args=(camera,client,D_addr,))   # target: 是通过run()方法调用的可调用对象,args：元组参数，为target所调用的
         clientThread.start()