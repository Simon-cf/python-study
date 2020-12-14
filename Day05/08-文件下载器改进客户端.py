"""
1.导入模块
2.创建套接字
3.建立连接
4.发送文件名
5.接收数据文件内容，保存到本地文件（循环）
6.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
re_addr = ('172.20.10.2', 3000)
tcp_client_socket.connect(re_addr)
# 4.发送文件名
fileName = input("请输入您想要下载的文件名：")
tcp_client_socket.send(fileName.encode())
# 5.接收数据文件内容，保存到本地文件（循环）
fileName = fileName[:-4] + "副本.txt"
with open(fileName, 'wb') as fp:
    while True:
        recv_data = tcp_client_socket.recv(1024)
        if recv_data:
            print("接收中...")
            fp.write(recv_data)
        else:
            print("接收完毕")
            break
# 6.关闭套接字
tcp_client_socket.close()
