#-*-coding:utf-8-*-

from socket import *
import threading
import re



address='127.0.0.1'
port=6337
buffsize=1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(10)     #最大连接数

client_list=[]  # 已登录的用户

# user_list=[[2097557613, 123456], [2097557614, 123456], [2097557615, 123456], [2097557616, 123456], [2097557617,123456],[2097557618,123456]]
user_list=[[201813347, 123456], [201813348, 123456], [201813349, 123456], [201813350, 123456], [201813351, 123456], [201813352,123456]]
user_l=len(user_list)
user_client=[]
group_list=[['信息论群'], ['微机原理群'], ['通信电子线路群'], ['通信原理群']]


def login(logindata, clientsock):

    for x in range(0,user_l):
        print("登录请求"+str(logindata[1]))
        if len(user_client)>=1:
            ul=len(user_client)

            if str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])!=str(logindata[2]):
                login_bkinfo = 'false-pw'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])==str(logindata[2]):
                for user_cl in range(0, ul):
                    if str(user_client[user_cl][0]) == str(logindata[1]):
                        login_bkinfo = 'false-login'
                        clientsock.send(login_bkinfo.encode())
                        break
                    elif user_cl == ul - 1:
                        usercl=[]
                        usercl.append(logindata[1])
                        usercl.append(clientsock)
                        login_bkinfo = 'true'
                        user_client.append(usercl)
                        print(user_client)

                        clientsock.send(login_bkinfo.encode())
                break
            elif x==user_l-1:
                login_bkinfo = 'false-user'
                clientsock.send(login_bkinfo.encode())

        else:

            if str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])!=str(logindata[2]):
                login_bkinfo = 'false-pw'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])==str(logindata[2]):
                usercl=[]
                usercl.append(logindata[1])
                usercl.append(clientsock)
                login_bkinfo = 'true'
                user_client.append(usercl)
                print(user_client[0][1])

                '''p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                list = re.findall(p1, str(user_client[0][1]))
                print(list[1])
                list1 = list[1].split(',')
                print(list1[0])'''


                clientsock.send(login_bkinfo.encode())
                break
            elif x==user_l-1:
                login_bkinfo = 'false-user'
                clientsock.send(login_bkinfo.encode())


def tcplink(clientsock, clientaddress):
    group_l = len(group_list)
    while True:
        recvdata = clientsock.recv(buffsize).decode('utf-8')
        recvdata_list = recvdata.split('$%')  # 信息间隔符为空格
        print(recvdata_list)
        if str(recvdata_list[0]) == 'login':  # 处理登录消息
            login(recvdata_list, clientsock)

        elif str(recvdata_list[0]) == 'wechat_req':  # 处理群聊消息
            for y in range(0, group_l):
                if str(group_list[y][0]) == str(recvdata_list[1]):
                    requser = str(recvdata_list[2]) + ' ' + '加入群聊'
                    group_list[y].append(clientsock)
                    # print('my clientsock is : ' + str(clientsock))
                    print(group_list[y])
                    groupl = len(group_list[y])
                    print(groupl)
                    if True:                                            #  groupl>2
                        for h in range(1, groupl):
                            group_list[y][h].send(requser.encode())
                    break
        elif str(recvdata_list[0]) == 'wechat_quit':  # 处理群聊消息
            for y in range(0, group_l):
                if str(group_list[y][0]) == str(recvdata_list[1]):
                    requser = str(recvdata_list[2]) + ' ' + '退出群聊'
                    group_list[y].remove(clientsock)
                    print(group_list[y])
                    groupl = len(group_list[y])
                    if True:
                        for h in range(1, groupl):
                            group_list[y][h].send(requser.encode())
                    else:
                        clientsock.send(requser.encode())
                    break
        elif str(recvdata_list[0]) == 'wechat':
            for wl in range(0, group_l):
                if str(group_list[wl][0]) == str(recvdata_list[1]):  ###
                    senddata=str(recvdata_list[2])+":"+str(recvdata_list[3])
                    l = len(group_list[wl])
                    try:
                        if l >= 2:
                            for x in range(1, l):
                                group_list[wl][x].send(senddata.encode())
                        else:
                            clientsock.send(senddata.encode())
                            break
                        print("群聊信息" + str(senddata)+str(clientaddress))
                    except ValueError:
                        break
        elif str(recvdata_list[0]) == 'personal':   # 处理私聊消息
            user_cl = len(user_client)
            send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
            z = 1
            for pl in range(0, user_cl):
                if user_client[pl][0]==recvdata_list[2]:
                    for ql in range(0, user_cl):
                        if user_client[ql][0] == recvdata_list[1]:
                            user_client[ql][1].send(send_info.encode())
                    user_client[pl][1].send(send_info.encode())
                    print(clientaddress)
                    break
                elif z == user_cl:
                    back = str(recvdata_list[2])+'不在线'
                    backtext = 'personal$%'+recvdata_list[1]+'$%'+recvdata_list[2]+'$%'+back
                    print('sendback text is: ' + backtext)
                    clientsock.send(back.encode())
                z = z + 1
        elif str(recvdata_list[0]) == 'voicechat':   # 处理语音聊天消息
            length = len(recvdata_list)
            if str(recvdata_list[length-2]) == 'end':
                user_cl = len(user_client)  # list[1] sender  list[2] receiver
                # send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
                length = len(recvdata_list)
                z = 1
                for pl in range(0, user_cl):
                    if user_client[pl][0] == recvdata_list[2]:
                        p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                        list = re.findall(p1, str(user_client[pl][1]))
                        list1 = list[1].split(',')
                        result = ''.join(list1)
                        result = result + '$%' + 'ignore' +'$%'+'voicechat_accept'  # 发送给发起方
                        print(list1)

                        for ql in range(0, user_cl):
                            if user_client[ql][0] == recvdata_list[1]:
                                p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                                list = re.findall(p1, str(user_client[ql][1]))
                                list1 = list[1].split(',')
                                send_info = ''.join(list1)
                                if recvdata_list[length - 2] == 'end':
                                    send_info = ''.join('end')
                                send_info = send_info + '$%' + 'voicechat_request'  # 发送给接收方
                                print('send_info is:' + send_info)
                                user_client[pl][1].send(send_info.encode())
                                # user_client[ql][1].send(result.encode())
                        print(clientaddress)

                        break
                    elif z == user_cl:
                        back = str(recvdata_list[2]) + '不在线'
                        clientsock.send(back.encode())
                    z = z + 1
            else:
                user_cl = len(user_client)         # list[1] sender  list[2] receiver
                # send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
                length = len(recvdata_list)
                z = 1
                for pl in range(0, user_cl):
                    if user_client[pl][0] == recvdata_list[2]:
                        p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                        list = re.findall(p1, str(user_client[pl][1]))
                        list1 = list[1].split(',')
                        result = ''.join(list1)
                        result = result + '$%' + 'voicechat_accept'  # 发送给发起方
                        print(list1)

                        for ql in range(0, user_cl):
                            if user_client[ql][0] == recvdata_list[1]:
                                p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                                list = re.findall(p1, str(user_client[ql][1]))
                                list1 = list[1].split(',')
                                send_info = ''.join(list1)
                                if recvdata_list[length-2] == 'end':
                                    send_info = ''.join('end')
                                send_info = send_info + '$%' + 'voicechat_request'   # 发送给接收方
                                print('send_info is:' + send_info)
                                user_client[pl][1].send(send_info.encode())
                                user_client[ql][1].send(result.encode())
                        print(clientaddress)

                        break
                    elif z == user_cl:
                        back = str(recvdata_list[2])+'不在线'
                        clientsock.send(back.encode())
                    z = z + 1
        elif str(recvdata_list[0]) == 'filesend':   # 处理文件传输
            user_cl = len(user_client)  # list[1] sender  list[2] receiver
            # send_info = str(recvdata_list[1])+":"+str(recvdata_list[3])
            z = 1
            for pl in range(0, user_cl):
                if user_client[pl][0] == recvdata_list[2]:
                    p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                    list = re.findall(p1, str(user_client[pl][1]))
                    list1 = list[1].split(',')
                    result = ''.join(list1)
                    result = result + '$%' + 'filesend_accept'
                    print(list1)

                    for ql in range(0, user_cl):
                        if user_client[ql][0] == recvdata_list[1]:
                            p1 = re.compile(r'[(](.*?)[)]', re.S)  # 正则表达式提取客户端的地址
                            list = re.findall(p1, str(user_client[ql][1]))
                            list1 = list[1].split(',')
                            send_info = ''.join(list1)
                            send_info = send_info + '$%' + 'filesend_request'
                            print('send_info is:' + send_info)
                            user_client[pl][1].send(send_info.encode())
                            user_client[ql][1].send(result.encode())
                    print(clientaddress)

                    break
                elif z == user_cl:
                    back = str(recvdata_list[2]) + '不在线'
                    clientsock.send(back.encode())
                z = z + 1
        elif str(recvdata_list[0]) == '':
            print('无法识别：')
            print(recvdata_list[0])
            break

    clientsock.close()
    del client_list[-1]


while True:
    clientsock, clientaddress = s.accept()
    client_list.append(clientsock)
    print('connect from:', clientaddress)   # clientaddress 包含IP与端口
    t = threading.Thread(target=tcplink, args=(clientsock,clientaddress))  #新创建的线程
    t.start()
# s.close()



