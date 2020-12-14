# 发送数据  方法.sendto()第一个参数对应的是发送数据的二进制格式用encode进行二进制编码，默认编码模式是utf-8
# 第二个参数是一个带有IP地址和端口号的元组

# 1.导入模块
import socket
# 2.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3.发送数据
text = "哈哈"
udp_socket.sendto(text.encode(), ("127.0.0.1", 8080))
# 4.关闭套接字
udp_socket.close()