"""
面向对象封装服务器

"""

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
import sys


class WebServer(object):
    """服务器类"""

    def __init__(self, port):
        """初始化服务器内容，得到服务器套接字"""

        # 2.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3.绑定端口
        local_addr = ('', port)
        tcp_server_socket.bind(local_addr)
        # 4.设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 5.设置监听
        tcp_server_socket.listen(20)

        self.tcp_server_socket = tcp_server_socket

        # 初始化游戏目录
        game_dict = dict()
        game_dict['2048'] = '2048'
        game_dict['塔防'] = 'tafang'
        game_dict['读心术'] = 'dxs'
        game_dict['植物大战僵尸'] = 'zwdzjs-v1'
        game_dict['植物大战僵尸外挂版'] = 'zwdzjs-v2'

        # 得到键
        key_list = list(game_dict.keys())
        for index, key in enumerate(key_list):
            print("%d.%s" % (index, key))
        # 捕获用户输入
        order = input("请选择您要玩的游戏：")
        # 根据编号得到游戏对应的键
        key_tul = key_list[int(order)]

        # 根据键得到对应的值，并且得到文件对应的路径
        current_dir = game_dict[key_tul] + "/index.html"
        self.current_dir = current_dir


    def request_handler(self, new_client_socket, ip_port):
        # 拼接响应报文 ，返回拼接好的响应报文

        # 得到请求的路径
        current_dir = self.current_dir
        if not current_dir:
            return
        # 9.拼接响应报文
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server:erqi/2.0\r\n"
        response_space = "\r\n"

        with open(current_dir, 'r', encoding='utf-8') as fp:
            response_body = fp.read()

        response_data = response_line + response_header + response_space + response_body
        return response_data.encode()

    def start(self):
        """主程序，启动服务器"""
        while True:
            # 6.接受连接，返回新的套接字和端口
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("服务器%s 来了" % str(ip_port))
            while True:
                # 处理请求得到响应报文
                response_data = self.request_handler(new_client_socket, ip_port)
                if not response_data:
                    break
                # 10.发送响应报文
                new_client_socket.send(response_data)
            # 11.关闭新套接字
            new_client_socket.close()
        # 12.关闭套接字
        # tcp_server_socket.close()


def main():
    # 根据sys获取命令行参数列表
    if len(sys.argv) != 2:
        print("命令格式错误：参考格式【python  文件名  端口号】")
    if not sys.argv[-1].isdigit():
        print("端口号格式错误，不是一个纯数字！")
    ws = WebServer(int(sys.argv[-1]))
    ws.start()


if __name__ == '__main__':
    main()
