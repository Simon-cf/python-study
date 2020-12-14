def app(request_data):
    """拼接响应报文"""
    request_url = request_data.decode().split(" ", 2)[1]
    if request_url == "/":
        request_url = '/index.html'
    print(request_url)
    # 8.拼接响应报文

    # 8.2 响应头
    response_header = "Server:cuifan.com\r\nStatus:200 OK\r\n"
    # 8.3 响应空行
    response_space = "\r\n"
    # 8.4 响应体
    try:
        with open('.' + request_url, 'rb') as fp:
            response_body = fp.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = ("Error!!! %s" % e).encode()
    else:
        # 8.1 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
    # response_body = ""
    response_data = (response_line + response_header + response_space).encode() + response_body
    return response_data