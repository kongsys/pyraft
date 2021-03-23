import socket
import sys

server_address = ("localhost", 10000)
print(f"starting up on {server_address[0]} port {server_address[1]}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)

sock.listen(1)

while True:
  print("waiting for connection")

  conn, addr = sock.accept()

  try:
    print(f"connection from {addr}")

    while True:
      data = conn.recv(16)
      print(f"received {data}")
      if data:
        print(f"sending data back to the client")
        conn.sendall(data)
      else:
        print(f"no more data from {addr}")
        break
  finally:
    conn.close()
