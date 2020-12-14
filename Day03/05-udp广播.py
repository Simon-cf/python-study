"""
1。导入模块
2.创建套接字
设置套接字，允许发送广播
3.发送广播
4.关闭套接字
"""


import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

addr = ('255.255.255.255', 9090)
message = "凡哥哥来了"
udp_socket.sendto(message.encode(), addr)

udp_socket.close()


