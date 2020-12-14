# udp聊天器
"""
1.导入模块
2.创建套接字（绑定端口）
3.发送数据
4.接收数据
5.关闭套接字
"""



# 1.导入模块
import socket
# 2.创建套接字（绑定端口）
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_addr = ('', 3213)
udp_socket.bind(local_addr)
# 3.发送数据
re_addr = ('172.20.10.1', 5000)
passage = input("请输入您想要发送的内容：")
print("等待服务器响应中...")
udp_socket.sendto(passage.encode(), re_addr)
# 4.接收数据
recv_data, ip_port= udp_socket.recvfrom(1024)
recv_text = recv_data.decode()

print("\n收到来自服务器的消息：<%s>\n" % recv_text)

# 5.关闭套接字
udp_socket.close()