import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('localhost', 10000)

sock.connect(server_addr)

try:
  msg = input("Type your message:\n")

  print(f"sending {msg}")
  sock.sendall(msg.encode('utf-8'))

  received = 0
  expected = len(msg)

  while received < expected:
    data = sock.recv(16)
    received += len(data)
    print(f"received {data}")

finally:
  print("closing socket")
  sock.close()
