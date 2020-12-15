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
from game_app import app
import sys


class WebServer(object):
    """服务器"""

    def __init__(self, ip, port):
        # 2.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3.绑定端口
        local_addr = (ip, int(port))
        tcp_server_socket.bind(local_addr)
        # 4.设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 5.设置监听
        tcp_server_socket.listen(20)
        self.tcp_server_socket = tcp_server_socket

        # 初始化项目
        self.projects_dict = dict()
        # 初始化字典值
        self.projects_dict['植物⼤战僵⼫-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物⼤战僵⼫-外挂版'] = "zwdzjs-v2"
        self.projects_dict['保卫萝⼘'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读⼼术'] = "dxs"

        # 初始化菜单
        self.init_menus()

    def init_menus(self):

        # 1.获取字典所有的key
        dict_keys = tuple(self.projects_dict.keys())
        # 2.输入提示信息
        print("请选择要发布的项目：\n")
        # 3.输出项目列表
        for index, key in enumerate(dict_keys):
            print("%d.%s" % (index, key))
        # 4.接受用户的输入
        sel_num = int(input("请输入您想要玩的游戏编号："))
        # 5.根据编号得到key
        sel_key = dict_keys[sel_num]
        # 6、根据字典key获取当前发布的项⽬的⽬录
        # 7、保存项⽬⽬录到实例变量中
        self.current_dir = self.projects_dict[sel_key]

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


def main():
    # 1、导⼊sys
    # 模块
    # 2、通过sys.argv
    # 获取参数列表
    # 3、判断列表⻓度是否为
    # 2 ，如果不等于2
    # 要给出提示，Web服务器启动失败
    # 4、取出第⼆个参数，判断是否是⼀个数字，如果不是⼀个数组，则给出提示，Web服务器启动
    # 失败5、接收启动参数
    # 端⼝号
    # 6、修改类构造⽅法，使⽤提供的端⼝号启动Web服务器
    if len(sys.argv) != 2:
        print("启动失败，参数个数错误，正确示范：python xxx.py 端口号")
        return
    if not sys.argv[-1].isdigit():
        print("端口号输入错误，应当为纯数字")
        return
    else:
        port = sys.argv[-1]
    ws = WebServer('172.20.10.2', port)
    ws.start()


if __name__ == '__main__':
    main()
