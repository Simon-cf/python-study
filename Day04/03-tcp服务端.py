"""
1.导入模块
2.创建套接字
# 绑定端口
3.设置监听
4.接受连接，返回新创建的套接字
5.接收数据
6.发送数据
7.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 绑定端口
local_addr = ('', 9000)
tcp_server_socket.bind(local_addr)
# 3.设置监听(控制客户端连接，确保客户端连接之后，能够分配新的套接字用来数据的收发)
tcp_server_socket.listen()
# 4.接受连接，返回新创建的套接字
new_socket, ip_port = tcp_server_socket.accept()
# 5.接收数据
recv_data = new_socket.recv(1024)
recv_text = recv_data.decode()
print("收到来自%s 的信息【%s】" % (ip_port, recv_text))
# 6.发送数据
message = input("请输入您想要发送的内容:")
new_socket.send(message.encode())
# 7.关闭套接字
new_socket.close()
tcp_server_socket.close()
