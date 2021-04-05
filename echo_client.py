import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('localhost', 10000)

sock.connect(server_addr)

while True:
  try:
    msg = input("Type your message:\n")
    print(f"sending {msg}")
    sock.sendall(msg.encode('utf-8'))

    data = sock.recv(1024)
    print(f"received {data}")

  except:
    print("closing socket")
    sock.close()
    break
