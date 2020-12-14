"""
1.导入模块
2.创建套接字（绑定端口）
3.设置监听，变主动为被动
4.接受连接，返回新的套接字和端口
5.接收文件名
6.打开文件并发送文件内容（循环）
7.关闭新套接字
"""

#
# 1.导入模块
import socket
# 2.创建套接字（绑定端口）
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_addr = ('172.20.10.2', 3000)
tcp_server_socket.bind(local_addr)
# 3.设置监听，变主动为被动
tcp_server_socket.listen(20)
print("服务器启动成功，可以下载文件了。")
while True:
    # 4.接受连接，返回新的套接字和端口
    new_socket, ip_port = tcp_server_socket.accept()
    print("新的客户端%s连接至服务器" % str(ip_port))
    # 5.接收文件名
    fileName = new_socket.recv(1024)
    # 6.打开文件并发送文件内容（循环）
    with open(fileName, 'rb') as fp:
        while True:
            fp_data = fp.read(1024)

            if fp_data:
                new_socket.send(fp_data)
                print("文件发送中...")
            else:
                print("发送成功！")
                break
    # 7.关闭新套接字
    new_socket.close()