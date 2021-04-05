import socket
from msg import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('localhost', 10000)

sock.connect(server_addr)

while True:
  try:
    msg = input("Type your message:\n")
    print(f"sending {msg}")
    send_msg(sock, msg.encode('utf-8'))

    data = recv_msg(sock)
    print(f"received {data}")

  except:
    print("closing socket")
    sock.close()
    break
