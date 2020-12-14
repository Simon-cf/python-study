"""
1.导入模块
2.创建套接字
3.建立连接
4.发送文件名
5.打开文件，并接收数据保存到本地
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
fileName = input("亲输入您想要下载的文件名：")
tcp_client_socket.send(fileName.encode())
# 5.打开文件，并接收数据保存到本地
with open(fileName[:-4] + "副本.txt", 'wb') as fp:
    while True:
        recv_data = tcp_client_socket.recv(1024)
        if recv_data:
            fp.write(recv_data)
        else:
            print("写入完成！")
            break
# 6.关闭套接字
tcp_client_socket.close()
