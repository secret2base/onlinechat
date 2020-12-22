import socket
import easygui as eg
import os
import time
import threading
from thread_result import MyThread
class file_send():
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.client.connect((self.ip, self.port))
        msg = self.client.recv(1024)
        print(msg.decode('utf-8'))

    def file_send_start(self):
        '''选择发送的文件'''
        filepath = eg.fileopenbox(title='选择文件')
        '''获取文件名,文件大小'''
        filename = filepath.split("\\")[-1]
        filesize = os.path.getsize(filepath)
        # 先将文件名传过去
        # 编码文件名
        self.client.send(filename.encode())
        time.sleep(0.5)
        # 再将将文件大小传过去
        # 编码文件大小
        self.client.send(filesize.to_bytes(filesize.bit_length(), byteorder='big'))
        try:
            '''传输文件'''
            start_time = time.time()
            with open(filepath, 'rb') as f:
                size = 0
                while True:
                    # 读取文件数据，每次1024KB
                    f_data = f.read(1024)
                    # 数据长度不为零，传输继续
                    if f_data:
                        self.client.send(f_data)
                        size += len(f_data)
                        if time.time() - start_time == 0:
                            time.sleep(0.5)
                        speed = (size) / (time.time() - start_time)
                        print('\r' + '【上传进度】:%s%.2f%%, Speed: %.2fMB/s' % (
                        '>' * int(size * 50 / filesize), float(size / filesize * 100), float(speed / 1024 / 1024)),
                              end=' ')
                    # 数据长度为零传输完成
                    else:
                        print(f'{filename},{float(filesize / 1024 / 1024):.2f}MB, 传输完成')
                        break
        except Exception as e:
            print(f'传输异常', e)
        self.client.close()
        return 0

class file_recv:
    def __init__(self):
        self.dirsave = "C:/Users/Public/Downloads/pythonqq_filerecv"
        if not os.path.exists(self.dirsave):  # 看是否有该文件夹，没有则创建文件夹
            os.mkdir(self.dirsave)
        ''' 创建socket对象'''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        '''获取本地'''
        # self.host = socket.gethostbyname(socket.gethostname())
        # print('self.host' + self.host)
        self.host = '127.0.0.1'

        '''设置端口'''
        self.port = 7788

        '''绑定地址'''
        self.server.bind((self.host, self.port))

        '''设置最大连接数， 超过后排队'''
        self.server.listen(12)

        print('服务器已上线\n等待客户端连接...\n')

    def server100(self):
        while True:
            '''建立客户端连接'''
            client, addr = self.server.accept()
            print(f'客户端: {str(addr)}, 连接上服务器')
            msg = f'已连接到服务器{self.host}!\r\n'
            client.send(msg.encode('utf-8'))
            # 有客户端连接后，创建一个线程给客户端
            t1 = MyThread(self.taskfilethread(client), args=(1, 2))
            # 设置线程守护
            t1.setDaemon(True)
            # 启动线程
            t1.start()
            t1.join()
            print(t1.get_result())

    def taskfilethread(self, client):
        '''接收文件名,文件大小'''
        filename = client.recv(1024)
        # time.sleep(0.5)
        filesize = client.recv(1024)
        # 解码文件名,文件大小
        filename = filename.decode()
        filesize = int.from_bytes(filesize, byteorder='big')
        '''接收文件'''
        try:
            f = open(self.dirsave+"\\"+ filename, 'wb')
            size = 0
            start_time = time.time()
            while True:
                # 接收数据
                f_data = client.recv(1024)
                # 数据长度不为零，接收继续
                if f_data:
                    f.write(f_data)
                    size += len(f_data)
                    if time.time() - start_time == 0:
                        time.sleep(0.5)
                    speed = (size) / (time.time() - start_time)
                    print('\r' + '【下载进度】:%s%.2f%%, Speed: %.2fMB/s' % ('>' * int(size * 50 / filesize), float(size / filesize * 100), float(speed/1024/1024)),end=' ')
                # 数据长度为零接收完成
                else:
                    break
        except Exception as e:
            print(f'接收异常', e)
        else:
            f.flush()
            print(f'{filename},{float(filesize/1024/1024):.2f}MB, 接收完成')
            f.close()
            return True

if __name__ == '__main__':

    fl = file_send('127.0.0.1', 7788)
    fl.file_send_start()