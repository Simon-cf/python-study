"""响应固定数据服务器
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听，变主动为被动
5.接受连接，返回分配新的套接字和端口
6.接受请求报文
7.拼接响应报文
8.返回响应报文
9.关闭新套接字
10.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ('10.164.0.148', 3000)
tcp_server_socket.bind(local_addr)
# 4.设置监听，变主动为被动
tcp_server_socket.listen(20)
# 5.接受连接，返回分配新的套接字和端口
new_socket, ip_port = tcp_server_socket.accept()
print("新客户端%s来了" % str(ip_port))
# # 6.接受请求报文
request_data = new_socket.recv(2048)
# print(request_data.decode())
# 7.拼接响应报文
response_line = "HTTP/1.1 200 OK\r\n"
response_header = "Server:BWS/2.0\r\n"
with open('Simon-cf.html', 'rb') as fp:
    data = fp.read()
    print(data)
response_data = response_line + response_header + "\r\n" + data.decode()
# 8.发送响应报文
new_socket.send(response_data.encode())
# 9.关闭新套接字
new_socket.close()
# 10.关闭套接字
tcp_server_socket.close()
