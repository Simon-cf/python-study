"""
1.导入模块
2.创建套接字
3.绑定端口
4.设置地址重用
5.设置监听
6.接受连接
7.接受请求报文
8.拼接响应报文
9.发送响应报文
10.关闭连接
11.关闭服务器
"""

# 1.导入模块
import socket
from application import app


class WebServer(object):
    """服务器"""

    def __init__(self, ip, port):
        # 2.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3.绑定端口
        local_addr = (ip, port)
        tcp_server_socket.bind(local_addr)
        # 4.设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 5.设置监听
        tcp_server_socket.listen(20)
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        """主函数"""

        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户来了:", ip_port)
            # 调用功能函数处理请求并且响应
            self.request_handler(new_client_socket, ip_port)
        # 11.关闭服务器
        # tcp_server_socket.close()

    def request_handler(self, new_socket, ip_port):
        """处理请求"""
        # 7.接受请求报文
        request_data = new_socket.recv(2048)
        if not request_data:
            print("客户端%s已经下线" % str(ip_port))
            new_socket.close()
            return

        response_data = app(request_data)
        # 9.发送响应报文
        new_socket.send(response_data)
        # 10.关闭连接
        new_socket.close()




if __name__ == '__main__':
    ws = WebServer('172.20.10.2', 3000)
    ws.start()
