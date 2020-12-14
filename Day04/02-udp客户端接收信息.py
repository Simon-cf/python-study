"""
1.导入模块
2.创建套接字
3.绑定端口
4.建立连接
5.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ("", 4000)
tcp_socket.bind(local_addr)
# 4.建立连接
re_addr = ("127.0.0.1", 7777)
tcp_socket.connect(re_addr)
# 5.发送消息
message = input("请输入您想要发送的信息：")
tcp_socket.send(message.encode())
# 6.接受信息
recv_data = tcp_socket.recv(1024)
recv_text = recv_data.decode('gbk')
print("接收到了消息：[%s]" % recv_text)
# 7.关闭套接字
tcp_socket.close()
