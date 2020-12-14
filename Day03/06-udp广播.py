"""
1.导入模块
# 1.导入模块
2.创建套接字
3.设置套接字，让其能够发送广播
4.发送广播（向255.255.255.255）
5.关闭套接字
"""

import socket

# 2.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3.设置套接字，让其能够发送广播
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
# 4.发送广播（向255.255.255.255）
message = "凡哥哥"
udp_socket.sendto(message.encode(), ("255.255.255.255", 8081))
# 5.关闭套接字
udp_socket.close()
