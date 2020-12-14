import socket

# 1.导入模块
# 2.创建套接字（指定传输协议（IPV4，socket.AF_INET,IPV6  socket.AF_INET6）, 传输方式(udp,socket.SOCK_DGRAM, tcp,socket.SOCK_STREAM)）
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3.关闭套接字
udp_socket.close()