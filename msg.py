def send_msg(sock, msg):
  send_size(sock, len(msg))
  sock.sendall(msg)

def send_size(sock, n):
  sock.sendall(n.to_bytes(8, "big"))

def recv_msg(sock):
  n = recv_size(sock)
  msg = recv_exactly(sock, n)
  return msg

def recv_size(sock):
  msg = recv_exactly(sock, 8)
  return int.from_bytes(msg, "big")

def recv_exactly(sock, n):
  msg = b''
  while n > 0:
    chunk = sock.recv(n)
    if not chunk:
      raise IOError("Connection closed")
    msg += chunk
    n -= len(chunk)
  return msg
