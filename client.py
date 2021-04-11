import socket
from msg import *

class Client:
  def __init__(self, server_port=10000):
    self.server_port = server_port

  def start(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = ('localhost', self.server_port)

    print(f"connecting to {server_addr[0]} port {server_addr[1]}")

    self.sock.connect(server_addr)

    while True:
      try:
        msg = input("Type your message:\n")
        print(f"sending {msg}")

        send_msg(self.sock, msg.encode("utf-8"))

        data = recv_msg(self.sock)
        print(f"received {data}")

      except:
        print(f"closing socket")
        self.sock.close()
        break
