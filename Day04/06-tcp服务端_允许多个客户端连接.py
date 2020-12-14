"""
1.导入模块
2.创建套接字
3.设置监听
4.接受连接，返回新的套接字和端口
5.接收数据
6.发送数据
7.关闭套接字
"""

# 1.导入模块
import socket
# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_addr = ('', 6333)
tcp_server_socket.bind(local_addr)
# 3.设置监听
tcp_server_socket.listen()
# 设置中间值，实现服务器的关闭
server_close = 0
while True:
    # 4.接受连接，返回新的套接字和端口
    new_socket, ip_port = tcp_server_socket.accept()
    # 5.接收数据
    while True:
        recv_data = new_socket.recv(1024)
        if not recv_data:
            print("与%s的连接已经断开" % str(ip_port))
            break
        recv_text = recv_data.decode()
        print("你收到了来自%s的消息 【%s】" % (str(ip_port), recv_text))
        # 6.发送数据
        message = input("请输入您想发送给对方的内容：")
        print("等待客户端回应...")
        print()
        if message == "close the server":
            server_close = 1
            break
        elif message == "close" + str(ip_port):
            print("关闭了与%s的连接" % str(ip_port))
            new_socket.close()
        new_socket.send(message.encode())
    if server_close:
        server_close = 0
        break
# 7.关闭套接字
print("准备关闭服务器...")
print("关闭中...")
print("成功关闭！")
tcp_server_socket.close()

# 不是完整版有bug，