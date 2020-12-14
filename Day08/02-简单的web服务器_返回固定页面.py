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


def request_handler(new_socket, ip_port):
    """处理请求"""
    # 7.接受请求报文
    request_data = new_socket.recv(2048)
    if not request_data:
        print("客户端%s已经下线" % str(ip_port))
        new_socket.close()
        return
    print(request_data.decode())
    # 8.拼接响应报文
    # 8.1 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 8.2 响应头
    response_header = "Server:cuifan.com\r\nStatus:200 OK\r\n"
    # 8.3 响应空行
    response_space = "\r\n"
    # 8.4 响应体
    with open('erqi_web.html', 'rb') as fp:
        response_body = fp.read()
    # response_body = ""
    response_data = (response_line + response_header + response_space).encode() + response_body
    # 9.发送响应报文
    new_socket.send(response_data)
    # 10.关闭连接
    new_socket.close()


def main():
    """主函数"""
    # 2.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3.绑定端口
    local_addr = ('172.20.10.2', 3000)
    tcp_server_socket.bind(local_addr)
    # 4.设置地址重用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 5.设置监听
    tcp_server_socket.listen(20)
    # 6.接受连接
    new_socket, ip_port = tcp_server_socket.accept()
    request_handler(new_socket, ip_port)
    # 11.关闭服务器
    # tcp_server_socket.close()

if __name__ == '__main__':
    main()
