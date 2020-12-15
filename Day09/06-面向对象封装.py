"""

能够实现 根据浏览器不同请求 返回对应⽹⻚资源 的Web服务器
1、Web服务器能够绑定固定端⼝
2、Web服务器端能够接收浏览器请求
3、Web服务器遵守HTTP协议，根据请求返回指定的html 内容给浏览器
4、当浏览器关闭后，Web服务器能够显示断开连接
5、Web服务器短时间内重启，不会提示 address already in use 错误
"""

"""
实现思路：
初始化部分：
1.导入模块
2.创建套接字
3.绑定端口
4.设置地址重用
5.设置监听

与客户端交互部分：
6.接受请求报文
7.解析请求报文，得到请求的文件路径
8.拼接响应报文
9.发送响应报文
10.关闭新套接字
"""

import socket
from app import application
import sys

# 初始化部分：
# 1.导入模块

class WebServer(object):

    def __init__(self, port):
        """定义初始化方法"""
        # 2.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3.绑定端口
        local_addr = ('', port)
        tcp_server_socket.bind(local_addr)
        # 4.设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 5.设置监听
        tcp_server_socket.listen(128)

        self.tcp_server_socket = tcp_server_socket

    def start(self):
        """启动服务器方法"""
        while True:
            # 6.接受客户端连接
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户端%s上线" % str(ip_port))
            self.request_handler(new_client_socket, ip_port)

    def request_handler(self, new_client_socket, ip_port):
        """定义相应服务器方法"""
        # 6.接受请求报文
        request_data = new_client_socket.recv(2048)
        # print(request_data)
        if not request_data:
            print("客户端%s连接已经断开！" % str(ip_port))
            new_client_socket.close()
            return

        response_data = application(request_data)
        # 9.发送响应报文
        new_client_socket.send(response_data)
        # 10.关闭新套接字
        new_client_socket.close()


def main():
    """主入口方法"""
    if len(sys.argv) != 2:
        print("启动失败，参数个数错误！正确格式:python xxx.py 8080")
        return
    if not sys.argv[1].isdigit():
        print("启动失败，端⼝不是数字!")
        return
    port = int(sys.argv[-1])
    ws = WebServer(port)
    ws.start()



if __name__ == '__main__':
    main()
