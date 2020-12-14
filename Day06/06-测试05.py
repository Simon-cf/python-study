"""
1.导入模块
2.创建套接字
3.建立连接
4.拼接请求报文
5.发送请求报文
6.得到响应报文
7.解析响应报文
8.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
re_addr = ("172.20.10.1", 4399)
tcp_client_socket.connect(re_addr)
# 4.拼接请求报文
request_line = "GET /HTTP/1.1\r\n"
request_header = "Connection: keep-alive\r\n"
request_data = request_line + request_header + "\r\n\r\n"
# 5.发送请求报文
tcp_client_socket.send(request_data.encode())
# 6.得到响应报文
response_data = tcp_client_socket.recv(9000)
print(response_data.decode())
# 7.解析响应报文
# 8.关闭套接字
tcp_client_socket.close()
