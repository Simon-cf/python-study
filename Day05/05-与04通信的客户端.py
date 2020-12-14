"""
1.导入模块
2.创建套接字
3.建立连接
4.发送数据
5.接收数据
6.关闭套接字
"""


# 1.导入模块
import socket
import time
# 2.创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
re_addr = ('172.20.10.2', 6969)
tcp_socket.connect(re_addr)
while True:
    # 4.发送数据
    message = input("请输入您想要发送给服务器的信息：")
    if message == "close the link":
        print("准备断开与服务器的连接...")
        time.sleep(1)
        print("断开成功！")
        break
    print("等到服务器响应中...")
    tcp_socket.send(message.encode())
    # 5.接收数据
    recv_data = tcp_socket.recv(1024)
    if not recv_data:
        print("服务器已经关闭,本程序即将关闭")
        print("套接字关闭，释放内存中...")
        time.sleep(2)
        print("关闭成功！")
        break
    recv_text = recv_data.decode()

    print("\n收到服务端发来的信息：【%s】\n" % recv_text)
# 6.关闭套接字
tcp_socket.close()