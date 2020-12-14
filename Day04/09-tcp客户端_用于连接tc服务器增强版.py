"""
1.导入模块
2.创建套接字
3.建立连接
4.发送数据
5.接收数据
6.关闭套接字

"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
re_addr = ('127.0.0.1', 6464)
tcp_client_socket.connect(re_addr)
# 4.发送数据
message = input("请输入您想要发送的数据：")
print("等待服务器的响应...")
print()
tcp_client_socket.send(message.encode())
# 5.接收数据
recv_data = tcp_client_socket.recv(1024)
recv_text = recv_data.decode()
print("收到服务器的回应：%s" % recv_text)
print()
# 6.关闭套接字
tcp_client_socket.close()
