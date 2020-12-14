
"""
导入模块
创建套接字
发送广播
关闭套接字"""

# 导入模块
import socket
# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置允许发送广播
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
# 发送广播
broadcast_addr = ('255.255.255.255', 9000)
send_content = input("请输入你想要广播的内容：")
udp_socket.sendto(send_content.encode(), broadcast_addr)
# 关闭套接字
udp_socket.close()
