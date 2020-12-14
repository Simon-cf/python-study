"""
1、Web服务器能够绑定固定端⼝
2、Web服务器端能够接收浏览器请求
3、Web服务器遵守HTTP协议，根据请求返回指定的html 内容给浏览器
4、当浏览器关闭后，Web服务器能够显示断开连接
5、Web服务器短时间内重启，不会提示 address already in use 错误
"""
"""
1.导入模块
2.创建套接字
3.绑定端口
4.设置监听
5.接受连接，返回新的套接字和端口
6.接受请求报文
7.拼接响应报文
8.发送响应报文
9.关闭套接字

"""


# 1.导入模块
import socket
# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ('172.20.10.2', 3000)
tcp_server_socket.bind(local_addr)
# 4.设置监听
tcp_server_socket.listen(3)
# 设置地址重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
while True:
    # 5.接受连接，返回新的套接字和端口
    new_socket, ip_port = tcp_server_socket.accept()
    # 6.接受请求报文
    request_data = new_socket.recv(2048)
    print(request_data.decode())
    # 7.拼接响应报文
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:erqi/1.0r\r\nStatus:200 OK\r\n"
    response_space = "\r\n"
    response_body = "hello world"
    response_data = response_line + response_header + response_space + response_body
    # 8.发送响应报文
    new_socket.send(response_data.encode())
    # 9.关闭套接字
    new_socket.close()

