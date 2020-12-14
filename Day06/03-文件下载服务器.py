"""

1.导入模块
2.创建套接字
3.绑定端口
4.设置监听，便主动为被动
5.接受连接，返回新的套接字和端口
6.接受文件名
7.打开指定的文件，读取文件内容并且发送
8.关闭新的套接字
9.关闭套接字
"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.绑定端口
local_addr = ("172.20.10.2", 3000)
tcp_server_socket.bind(local_addr)
# 4.设置监听，便主动为被动
tcp_server_socket.listen(20)
while True:
    # 5.接受连接，返回新的套接字和端口
    new_socket, ip_port = tcp_server_socket.accept()
    print("新的客户端%s来了" % str(ip_port))
    # 6.接受文件名
    fileName = new_socket.recv(1024)
    if not fileName:
        print("客户端%s已经断开连接" % str(ip_port))
        new_socket.close()
    # 7.打开指定的文件，读取文件内容并且发送
    with open(fileName, 'rb') as fp:
        while True:
            send_data = fp.read(1024)
            if send_data:
                new_socket.send(send_data)
            else:
                print("发送成功！")
                break
    # 8.关闭新的套接字
    new_socket.close()
# 9.关闭套接字
# tcp_server_socket.close()