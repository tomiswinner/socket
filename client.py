import socket
import time

ip_address = 'localhost'
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((str(ip_address), 52001))

for i in range(10):  # change this number as needed
    message = 'Hello! This is message {}'.format(i)
    tcp_socket.send(message.encode("utf-8"))
    response = tcp_socket.recv(1024)
    print('Data : {}'.format(response.decode("utf-8")))
    time.sleep(1)  # optional delay between messages

tcp_socket.close()
