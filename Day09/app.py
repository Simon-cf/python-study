def parse_request(request_data):
    """处理客户端请求"""
    request_text = request_data.decode()
    # 7.解析请求报文，得到请求的文件路径
    request_url = request_text.split(' ', 2)[1]
    if request_url == "/":
        request_url += 'index.html'
    return request_url

def application(request_data):
    """解析请求报文"""
    request_url = parse_request(request_data)
    print(request_url)

    # 拼接响应报文
    response_header = "Server:erqi/1.1\r\n"
    response_space = "\r\n"

    # 判断请求的文件是否存在，存在就拼接返回，不存在返回error页面
    try:
        with open("." + request_url, 'rb') as fp:
            response_body = fp.read()
            response_body = response_body
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = "<h1>Error!!! %s</h1>" % e
        response_body = response_body.encode()
    else:
        response_line = "HTTP/1.1 200 Ok\r\n"

    response_data = (response_line + response_header + response_space).encode() + response_body
    return response_data