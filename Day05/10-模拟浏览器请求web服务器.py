"""
1.导入模块
2.创建套接字
3.连接服务器（DNS解析和连接HTTP服务器）
4.组装请求报文
5.发送请求报文
6.接收响应报文
7.解析响应报文
8.关闭套接字
"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.连接服务器（DNS解析和连接HTTP服务器）
tcp_client_socket.connect(("cf0527.3vdo.net", 80))
# 4.组装请求报文
# 4.1请求行
request_line = "GET / HTTP/1.1\r\n"
# 4.2请求头
request_header = "Host:www.baidu.com\r\n"
# 4.3请求空行
request_data = request_line + request_header + "\r\n"
# 4.4请求主体
# 5.发送请求报文
tcp_client_socket.send(request_data.encode())
# 6.接收响应报文
reponse_data = tcp_client_socket.recv(4096)
response_str_data = reponse_data.decode()
# 7.解析响应报文(可以使用正则表达式)
index = response_str_data.find("\r\n\r\n")
html = response_str_data[index + 4:]
with open('index.html', 'wb') as fp:
    fp.write(html.encode())
# 8.关闭套接字
print("模拟成功!")
tcp_client_socket.close()
