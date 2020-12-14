"""
1.导入模块
2.创建套接字
3.建立连接
4.发送数据
5.关闭套接字
"""

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect(("172.20.10.1", 9999))

message = input("请输入您想要发送的内容：")
tcp_socket.send(message.encode())
tcp_socket.close()
