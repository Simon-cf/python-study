"""
服务器功能，能够根据请求返回对应的页面
1.导入模块
2.创建套接字
3.绑定端口
4.设置地址重用
5.设置监听
6.接受连接，返回新的套接字和端口
7.接收请求报文
8.根据请求报文查找文件
9.拼接响应报文
10.发送响应报文
11.关闭新套接字
12.关闭套接字



"""

# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ('', 3000)
tcp_server_socket.bind(local_addr)
# 4.设置地址重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 5.设置监听
tcp_server_socket.listen(20)
while True:
    # 6.接受连接，返回新的套接字和端口
    new_client_socket, ip_port = tcp_server_socket.accept()
    while True:
        # 7.接收请求报文
        request_data = new_client_socket.recv(2048)
        if not request_data:
            print("客户端%s已经下线" % str(ip_port))
            break
        request_text = request_data.decode()
        print(request_text)
        # 8.根据请求报文获得请求路径
        current_dir = request_text.split(" ", 2)[1]
        if current_dir == "/":
            current_dir += 'index.html'
        print(current_dir)
        # 9.拼接响应报文
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server:erqi/2.0\r\n"
        response_space = "\r\n"

        with open("." + current_dir, 'r', encoding='utf-8') as fp:
            response_body = fp.read()

        response_data = response_line + response_header + response_space + response_body
        # 10.发送响应报文
        new_client_socket.send(response_data.encode())
    # 11.关闭新套接字
    new_client_socket.close()
# 12.关闭套接字
# tcp_server_socket.close()
