"""
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听，变主动为被动
5.接受连接，返回新的套接字和端口
6.接受请求数据，
7.打开指定文件，并返回指定文件
8.关闭新套接字
9.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ("172.20.10.2", 3000)
tcp_server_socket.bind(local_addr)
# 4.设置监听，变主动为被动
tcp_server_socket.listen(20)

# 5.接受连接，返回新的套接字和端口
new_socket, ip_port = tcp_server_socket.accept()
print("新客户端来了")
while True:
    # 6.接受请求数据，
    request_data = tcp_server_socket.recv(2048)
    if not request_data:
        break
    print(request_data)
    recv_text = request_data.decode()
    print(recv_text)
    # 7.打开指定文件，并返回指定文件
    fileName = "index.html"
    with open(fileName, 'rb') as fp:
        response_data = fp.read(4096)
        new_socket.send(response_data)
# 8.关闭新套接字
new_socket.close()
# 9.关闭套接字
# tcp_server_socket.close()
