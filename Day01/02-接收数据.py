import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto("hello world".encode(), ("127.0.0.1", 8080))
# 接收数据（参数为缓冲区大小，单位式字节）
data = udp_socket.recvfrom(1024)
# 接收到的数据是一个元组，第一个数据是二进制类型的数据，第二个参数是一个元组，里面包含发送方的IP和端口号
print("收到来自于 %s 的信息是：%s " % (data[1], data[0].decode(encoding='utf-8', errors='ignore')))
udp_socket.close()
