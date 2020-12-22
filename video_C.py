import socket
import cv2
import threading
import struct
import numpy

#TCP连接

#1.　客户端连接端口后，首先发送需要协商的分辨率和帧数，以致能够使传输“协议”一致

#2.　客户端使用线程，对图片进行收集

#3.　对收到的每一张图片进行解码，并利用OpenCV播放出来，即可实现C/S两端实时视频传输。

#4 利用服务器端打开端口8880，此时客户端连接后，便可以在客户端中捕获到服务器端的视频。


class Camera_Connect_Object:                                         #定义一个摄像头类
     def __init__(self,D_addr_port=["",8880]):                         #类的构造函数，当创建了这个类的实例时就会调用该方法
         self.resolution=[640,480]                                      #self 代表类的实例
         self.addr_port=D_addr_port                                     #绑定的端口和ip
         self.src=888+15                                                #双方确定传输帧数，（888）为校验值
         self.interval=0                                                #图片播放时间间隔
         self.img_fps=15                                                #每秒传输多少帧数


     def Socket_Connect(self):
         self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # 选择TCP连接方式
         self.client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)      # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
         self.client.connect(self.addr_port)                                   #连接对应的端口位置，包括IP和端口，传输给客户端
         print("IP is %s:%d" % (self.addr_port[0],self.addr_port[1]))          #输入连接的IP和端口号

     def RT_Image(self):
         self.name=self.addr_port[0]+" Camera"
         self.client.send(struct.pack("lhh", self.src, self.resolution[0], self.resolution[1]))     #按照格式打包发送帧数和分辨率
         while(1):
              info=struct.unpack("lhh",self.client.recv(8))                          #将接收到的8位二进制解包
              buf_size=info[0]                                                       #获取读的图片总长度
              if buf_size:
                  try:
                      self.buf=b""                #代表bytes类型
                      temp_buf=self.buf
                      while(buf_size):            #读取每一张图片的长度
                           temp_buf=self.client.recv(buf_size)
                           buf_size-=len(temp_buf)
                           self.buf+=temp_buf      #获取图片
                           data = numpy.frombuffer(self.buf, dtype='uint8')    #按uint8转换为图像矩阵
                           self.image = cv2.imdecode(data, 1)                  #图像解码
                           cv2.imshow(self.name, self.image)                   #展示图片
                  except:
                     pass;
                  finally:
                     if(cv2.waitKey(10)==27):                 #每10ms刷新一次图片，按‘ESC’（27）退出
                         self.client.close()
                         cv2.destroyAllWindows()
                         break
     def Get_Data(self,interval):
         showThread=threading.Thread(target=self.RT_Image)
         showThread.start()

if __name__ == '__main__':
     camera=Camera_Connect_Object()
     camera.addr_port[0]=input("Please input IP:")
     camera.addr_port=tuple(camera.addr_port)
     camera.Socket_Connect()
     camera.Get_Data(camera.interval)