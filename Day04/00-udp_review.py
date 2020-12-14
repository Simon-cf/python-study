"""

1.导入模块
2.创建套接字
3.发送信息
4.接收信息
5.关闭套接字
"""
import socket


def send_message(udp_socket):
    ip = input("请输入对方的ip地址：")
    port = input("请输入对方的端口号：")
    if not ip:
        ip = "172.20.10.2"
        print("您没有进行操作，默认把ip设置为{%s}" % ip)
    if not port:
        port = "3000"
        print("您没有进行操作，默认把ip设置为{%s}" % port)
    message = input("请输入您想要发送的内容：")
    udp_socket.sendto(message.encode(), (ip, int(port)))


def recv_message(udp_socket):
    recv_data, ip_port = udp_socket.recvfrom(1024)
    print("收到来自%s 的消息 【%s】" % (ip_port, recv_data.decode()))


def show_tips():
    print("*" * 30)
    print("1.发送消息".center(26))
    print("2.接收消息".center(26))
    print("3.退出系统".center(26))
    print("*" * 30)


if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('', 3000)
    udp_socket.bind(local_addr)
    while True:
        show_tips()
        num = int(input("请执行您想要进行的操作:"))
        if num == 1:
            send_message(udp_socket)
        elif num == 2:
            recv_message(udp_socket)
        elif num == 3:
            print("【感谢您的使用，再见！】")
            print("正在退出...")
            print("退出成功！")
            break
    udp_socket.close()
