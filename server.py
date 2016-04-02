import socket
sock = socket.socket()
sock.bind(('localhost',8000))
sock.listen(5)
buf_size = 2048

while 1:
    conn, addr = sock.accept()
    buf = conn.recv(buf_size)
    path = buf.split('\n')[0].split(' ')[1]
    path = path[1:]
    if path == "":
        path = "index.html"
    f = open(path, 'rb')
    conn.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + f.read())
    f.close()
    conn.close()
sock.close()