"""
1.导入模块
2.创建套接字（绑定端口）
3.设置监听，变主动为被动
4.接受连接，返回新的套接字和端口号
5.打开文件，读取内容并发送
6.关闭新的套接字
"""


# 1.导入模块
import socket
# 2.创建套接字（绑定端口）
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.设置监听，变主动为被动
local_addr = ('172.20.10.2', 3000)
tcp_server_socket.bind(local_addr)
tcp_server_socket.listen()
# 4.接受连接，返回新的套接字和端口号
new_socket, ip_port = tcp_server_socket.accept()
# 5.打开文件，读取内容并发送
# 接收数据
fileName = new_socket.recv(1024).decode()

with open(fileName, 'rb') as fp:
    while True:
        fp_data = fp.read(1024)
        if fp_data:
            new_socket.send(fp_data)
            print("发送中...")
        else:
            print("发送完毕")
            break
# 6.关闭新的套接字
new_socket.close()