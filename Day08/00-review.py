"""响应固定数据服务器
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听（变被动为主动）
5.接受请求，返回新的套接字和端口
6.接收请求报文
7.拼接响应报文
8.发送响应报文
9.关闭套接字

"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ("172.20.10.2", 3000)
tcp_server_socket.bind(local_addr)
# 4.设置监听（变被动为主动）
tcp_server_socket.listen(20)

# 5.接受请求，返回新的套接字和端口
new_socket, ip_port = tcp_server_socket.accept()
# while True:
# 6.接收请求报文
request_data = new_socket.recv(2048)
print(request_data.decode())
if not request_data:
    print("客户端%s已经断开连接" % str(ip_port))
# 7.拼接响应报文
response_line = "HTTP/1.1 200 OK\r\n"
response_header = "Server:erqi/2.0\r\n"
response_space = "\r\n"
# response_body = "<h1>Hello World!</h1>"
with open('erqi_web.html', 'r', encoding="utf-8") as fp:
    response_body = fp.read()
response_data = response_line + response_header + response_space + response_body
# print(response_data)
# 8.发送响应报文
new_socket.send(response_data.encode())
# 9.关闭套接字
new_socket.close()