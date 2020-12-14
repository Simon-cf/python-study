import socket


def send_message(udp_socket):
    addr_ip = input("请输入对方ip地址：\n")
    if len(addr_ip) == 0:
        addr_ip = '172.20.10.2'
        print("默认设置为{}".format(addr_ip))
    port = input("请输入对方端口号：\n")
    if not port:
        port = '8080'
        print("默认设置为{}".format(port))
    message = input("请输入您要发送的信息:\n")
    udp_socket.sendto(message.encode(), (addr_ip, int(port)))


def recv_message(udp_socket):
    recv_data, ip_port = udp_socket.recvfrom(1024)
    recv_text = recv_data.decode()
    print("接收到的消息为【{}】".format(recv_text))
    print("对方是{}".format(ip_port))


def show_tips():
    print("{:*^{}}".format("*", 25))
    print("{:*^{}}".format("  1.发送消息  ", 25))
    print("{:*^{}}".format("  2.接受消息  ", 25))
    print("{:*^{}}".format("  3.退出系统  ", 25))
    print("{:*^{}}".format("*", 25))


if __name__ == '__main__':
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口
    udp_socket.bind(('', 5001))

    while True:
        show_tips()
        num = int(input("请选择对应的功能："))
        if num == 1:
            send_message(udp_socket)
        elif num == 2:
            recv_message(udp_socket)
        elif num == 3:
            print("【欢迎您的使用，再见！】")
            break
    udp_socket.close()
