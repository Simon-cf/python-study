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
import time
# 2.创建套接字（绑定端口）
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_addr = ('', 3214)
udp_socket.bind(local_addr)
while True:
    # 4.接收数据
    recv_data, ip_port= udp_socket.recvfrom(1024)
    recv_text = recv_data.decode()

    print("\n收到来自%s的消息：<%s>\n" % (str(ip_port), recv_text))
    # 3.发送数据
    re_addr = ('172.20.10.2', 3213)
    passage = input("请输入您想要发送的内容：")
    if passage == "close the link":
        print("\n准备断开连接...")
        time.sleep(1)
        print("连接成功断开！")
        break
    print("等待服务器响应中...")
    udp_socket.sendto(passage.encode(), re_addr)

# 5.关闭套接字
udp_socket.close()