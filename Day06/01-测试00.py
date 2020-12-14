"""客户端
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
tcp_client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
re_addr = ("172.20.10.2", 3000)
tcp_client_server.connect(re_addr)
while True:
    # 4.发送数据
    message = input("请输入您想要发送的数据：")
    tcp_client_server.send(message.encode())
    if message == "close the link":
        print('已断开与客户端的连接！')
        break
    # 5.接收数据
    recv_data = tcp_client_server.recv(1024)
    recv_text = recv_data.decode()
    print(recv_text)
# 6.关闭套接字
tcp_client_server.close()