import socket
from application import app
import sys

class Webserver(object):
    """Webserver-web服务器类"""

    # 定义初始化方法
    def __init__(self):
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口
        local_addr = ('172.20.10.2', 3000)
        tcp_server_socket.bind(local_addr)
        # 设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 开启监听
        tcp_server_socket.listen(3)
        self.tcp_server_socket = tcp_server_socket

        # 初始化项目
