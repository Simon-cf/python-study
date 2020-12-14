"""
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听
5.接受连接，返回新的套接字和端口
6.接受请求报文
7.打开指定文件读取数据
8.拼接响应报文
9.发送指定响应报文
10.关闭新套接字
11.关闭套接字
"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ("127.0.0.1", 3000)
tcp_server_socket.bind(local_addr)
# 4.设置监听
tcp_server_socket.listen(20)
# 5.接受连接，返回新的套接字和端口
new_socket, ip_port = tcp_server_socket.accept()
# 6.接受请求报文
request_data = new_socket.recv(2048)
# 7.打开指定文件读取数据
fileName = "index.html"
with open(fileName, 'r',encoding="utf-8") as fp:
    # , encoding = 'utf-8'
    response_body = fp.read(4096)
# ?为什么不能编码
# 8.拼接响应报文
response_line = "HTTP/1.0 200 OK\r\n"
response_header = "Server:erqi/3.0\r\n"
response_data = response_line + response_header + "\r\n" + response_body
# 9.发送指定响应报文
new_socket.send(response_data.encode())
# 10.关闭新套接字
new_socket.close()
# 11.关闭套接字
tcp_server_socket.close()
