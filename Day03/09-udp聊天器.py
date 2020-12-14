import socket


def send_message(udp_socket):
    ip = input("请输入对方的ip地址:")
    if not ip:
        ip = "170.20.10.2"
        print("ip默认为{}".format(ip))
    port = input("请输入对方的端口号：")
    if not port:
        port = "8080"
        print("port默认为{}".format(port))
    message = input("请输入您想要发送的信息：")
    udp_socket.sendto(message.encode(), (ip, int(port)))


def recv_message(udp_socket):
    recv_data, ip_port = udp_socket.recvfrom(1024)
    print("收到来自{}的消息{}".format(ip_port, recv_data.decode()))


def show_tips():
    print("{:*>{}}".format("*", 40))
    print("{:*^{}}".format("  1.发送信息  ", 38))
    print("{:*^{}}".format("  2.接收信息  ", 38))
    print("{:*^{}}".format("  3.退出系统  ", 38))
    print("{:*>{}}".format("*", 40))


if __name__ == '__main__':
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口
    udp_socket.bind(('', 3000))

    while True:
        show_tips()
        num = int(input('请选择您要进行的操作：'))
        if num == 1:
            send_message(udp_socket)
        elif num == 2:
            recv_message(udp_socket)
        elif num == 3:
            print("【感谢您的使用，再见！】")
            print("正在退出...")
            print("已经成功退出...")
            break
    udp_socket.close()
