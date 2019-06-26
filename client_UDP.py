import time
from socket import *
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1.0)
message = 'ping'
addr = ("localhost", 12000)
for sequence_number in range(1,11):
    start = time.time()
    client_socket.sendto(message.encode(), addr)
    try:
        response_message, server = client_socket.recvfrom(1024)
        end = time.time()
        RTT = end - start
        #print(f'{response_message} {sequence_number} {RTT}')
        print('#%d'%sequence_number)
        print('Response_message:%s'%response_message)
        print('RTT:%fseconds'%RTT)
    except timeout:
        print('#%d'%sequence_number)
        print('Request timed out')
