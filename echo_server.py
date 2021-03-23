import socket
import sys

data = {}

def get(k):
  return data[k]

def set(k, v):
  data[k] = v

def delete(k):
  del data[k]

def run_server():
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
        op = conn.recv(16)
        str_op = op.decode("utf-8")
        print(f"received {str_op} of type {type(str_op)}")
        if op:
          cmd, key, v = 0, 1, 2
          operands = str_op.split(" ")
          resp = "Sorry, I don't understand taht command,"

          if operands[cmd] == "get":
            resp = get(operands[key])
          elif operands[cmd] == "set":
            set(operands[key], operands[v])
            resp = f"key {operands[key]} set to {operands[v]}"
          elif operands[cmd] == "delete":
            delete(operands[key])
            resp = f"key {key} deleted"
          elif operands[cmd] == "show":
            resp = str(data)
          else:
            pass
          conn.sendall(resp.encode("utf-8"))

        else:
          print(f"no more data from {addr}")
          break
    finally:
      conn.close()

run_server()
