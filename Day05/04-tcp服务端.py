"""
1.导入模块
2.创建套接字（绑定端口）
3.设置监听，把套接字变为被动
4.接受连接，为连接的客户端分配新的套接字，返回性能的套接字和端口
5.接收数据
6.发送数据
7.关闭新的套接字
8.关闭服务器套接字
"""


# 1.导入模块
import socket,time
# 2.创建套接字（绑定端口）
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_addr = ('172.20.10.2', 6969)
tcp_server_socket.bind(local_addr)
# 3.设置监听，把套接字变为被动
tcp_server_socket.listen()
print("服务器启动成功，等待客户端连接。")
while True:
    # 设置变量控制服务器开关
    order_shutdown = 0
    # 4.接受连接，为连接的客户端分配新的套接字，返回性能的套接字和端口
    new_socket, ip_port = tcp_server_socket.accept()
    print("\n新客户端%s成功连接到服务器\n" % str(ip_port))
    while True:
        # 5.接收数据
        recv_data = new_socket.recv(1024)
        if not recv_data:
            print("客户端%s已经关闭了与服务器的连接，服务器正在关闭给其分配的系统资源，释放内存...")
            time.sleep(1)
            print("关闭成功！")
            break
        recv_text = recv_data.decode()
        print("收到了来自%s发来的信息[%s]\n" % (str(ip_port), recv_text))
        # 6.发送数据
        message = input("请输入您想要发送给客户端信息：")
        if message == "root":
            order = input("请输入指令：")
            if order == "shutdown the server":
                order_shutdown = 1
                break
        elif not message:
            continue
        new_socket.send(message.encode())
        print("等待客户端%s回应...\n" % str(ip_port))
    # 7.关闭新的套接字
    new_socket.close()
    if order_shutdown:
        print("服务器即将关闭...")
        time.sleep(0.5)
        print("关闭中....")
        time.sleep(2)
        print("关闭成功！")
        break
# 8.关闭服务器套接字
tcp_server_socket.close()