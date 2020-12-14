"""
1.导入模块
2.创建套接字
3.开启监听，把套接字转换为被动模式
4.接受连接，返回新的套接字和端口
5.接收数据
6.发送数据
7.断开当前连接，关闭i新的套接字
8.关闭服务器
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
local_addr = ('', 6464)
tcp_server_socket.bind(local_addr)
# 3.开启监听，把套接字转换为被动模式
tcp_server_socket.listen()
while True:
    # 4.接受连接，返回新的套接字和端口
    new_socket, ip_port = tcp_server_socket.accept()
    while True:
        # 5.接收数据
        recv_data = new_socket.recv(1024)
        recv_text = recv_data.decode()
        print("收到客户端%s的消息【%s】" % (ip_port, recv_text))
        print()
        if not recv_data:
            # 7.断开当前连接，关闭新的套接字
            new_socket.close()
            break
        # 6.发送数据
        passage = input("请输入您想要发送的内容:")
        new_socket.send(passage.encode())
        print("等待客户端%s的请求..." % str(ip_port))
        print()

# 8.关闭服务器
# tcp_server_socket.close()
