from application import utils


def parse_request(request_data, ip_port):
    """ 解析请求的报文 返回客户端请求的资源路径"""
    # 根据客户端浏览器请求的资源路径，返回请求资源
    # 1）把请求协议解码，得到请求报文的字符串
    request_text = request_data.decode()
    # 2）得到请求行
    #    （1） 查找 第一个\r\n 出现的位置
    loc = request_text.find("\r\n")
    #    （2） 截取字符串，从开头截取到 第一个\r\n 出现的位置
    request_line = request_text[:loc]
    # print(request_line)
    # 3）把请求行，按照空格拆分，得到列表
    request_line_list = request_line.split(" ")
    # print(request_line_list)

    # 得到请求的资源路径
    file_path = request_line_list[1]
    print("[%s]正在请求:%s" % (str(ip_port), file_path))

    # 设置默认首页
    if file_path == "/":
        file_path = "/index.html"

    return file_path


def application(current_dir, request_data,ip_port):

    # 调用 parse_request函数，解析请求协议，返回请求的资源路径
    file_path = parse_request(request_data, ip_port)
    # 定义变量保存资源路径
    resource_path = current_dir+file_path


    try:
        # 通过 with open 读取文件
        with open(resource_path, "rb") as file:
            # 把读取的文件内容返回给客户端
            response_body = file.read()

        # 调用 utils 模块的 create_http_response 函数，拼接响应协议
        response_data = utils.create_http_response("200 OK", response_body)

    except Exception as e:

        # 2）响应的内容为错误
        response_body = "Error! (%s)" % str(e)
        # 3）把内容转换为字节码
        response_body = response_body.encode()
        # 调用 utils 模块的 create_http_response 函数，拼接响应协议
        response_data = utils.create_http_response("404 Not Found", response_body)

    return response_data