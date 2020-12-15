"""
测试00
1.导入模块
2.创建套接字
3.建立连接
4.发送数据
5.接收数据并保存到本地
6.关闭套接字
"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接
re_addr = ('127.0.0.1', 3000)
tcp_client_socket.connect(re_addr)
# 4.发送数据
request_url = input("请输入您想要访问的文件：(默认为'/')")
if not request_url:
    request_url = "/"
# 拼接请求报文
request_line = "GET %s HTTP/1.1\r\n" % request_url
request_header = "Host:192.168.0.117\r\n"
request_space = "\r\n"
request_data = request_line + request_header + request_space
# 发送响应报文
tcp_client_socket.send(request_data.encode())
# 5.接收数据并保存到本地
response_data = tcp_client_socket.recv(4096)
response_text = response_data.decode()

# print(response_text)
html = response_text.split('\r\n', 3)[-1]
print(html)

with open('index1.html', 'w', encoding='utf-8') as fp:
    fp.write(html)
# print(response_data.decode())
# 6.关闭套接字
tcp_client_socket.close()