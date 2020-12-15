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

# 初始化部分：
# 1.导入模块



def request_handler(new_client_socket):
    # 与客户端交互部分：
    # 6.接受请求报文
    request_data = new_client_socket.recv(2048)
    if not request_data:
        print("客户端连接已经断开！")
        new_client_socket.close()
        return
    request_text = request_data.decode()
    # 7.解析请求报文，得到请求的文件路径
    request_url = request_text.split(' ', 2)[1]
    if not request_url:
        print("用户请求报文格式错误！")
        new_client_socket.close()
        return
    if request_url == "/":
        request_url += 'index.html'
    print(request_url)

    # 响应报文
    response_header = "Server:erqi/1.1\r\n"
    response_space = "\r\n"

    # 判断请求的文件是否存在，存在就拼接返回，不存在返回error页面
    try:
        with open("." + request_url, 'r', encoding='utf-8') as fp:
            response_body = fp.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = "<h1>Error!!! %s</h1>" % e
    else:
        # 8.拼接响应报文
        response_line = "HTTP/1.1 200 Ok\r\n"

    response_data = response_line + response_header + response_space + response_body
    response_data = response_data.encode()
    # 9.发送响应报文
    new_client_socket.send(response_data)
    # 10.关闭新套接字
    new_client_socket.close()

def main():
    # 2.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3.绑定端口
    local_addr = ('', 3000)
    tcp_server_socket.bind(local_addr)
    # 4.设置地址重用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 5.设置监听
    tcp_server_socket.listen(128)

    while True:
        # 6.接受客户端连接
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("新客户端%s上线" % str(ip_port))
        request_handler(new_client_socket)

if __name__ == '__main__':
    main()


