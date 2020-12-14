"""
目标：创建服务器
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听，便主动为被动
5.接收连接，返回新的套接字和端口号
6.接收数据
7.发送响应数据
8.关闭新的套接字
9.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ('172.20.10.2', 3000)
tcp_server_socket.bind(local_addr)
while True:
    # 4.设置监听，便主动为被动
    tcp_server_socket.listen(20)
    while True:

        # 5.接收连接，返回新的套接字和端口号
        new_socket, ip_port = tcp_server_socket.accept()
        print("新的客户端%s来了" % str(ip_port))
        # 6.接收数据
        recv_data = new_socket.recv(1024)
        if not recv_data:
            print("客户端%s已经断开连接" % str(ip_port))
            break
        recv_text = recv_data.decode()
        print(recv_text)
        # 7.发送响应数据
        message = input("请输入您想要发送的内容：")
        new_socket.send(message.encode())
    # 8.关闭新的套接字
    new_socket.close()
# 9.关闭套接字
# tcp_server_socket.close()
