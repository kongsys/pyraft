import socket
import threading
from store import KVStore
from msg import *
import config

class Server:
  def __init__(self, name, port=10000):
    self.port = port
    self.name = name
    self.kvs = KVStore()
    self.catch_up(self.kvs)

  def start(self):
    server_addr = ('localhost', self.port)
    print(f"starting up on {server_addr[0]} port {server_addr[1]}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    sock.listen(1)

    while True:
      conn, addr = sock.accept()

      print(f"connection from {addr}")
      threading.Thread(target=handle_conn, args=(conn, self)).start()

  def handle_conn(self, conn, obj):
    try:
  
      while True:
        op = recv_msg(conn)
        if op:
          de_op = op.decode("utf-8")
          print(f"received {de_op}")
          with open("cmd.txt", "a") as f:
            f.write(de_op)
            f.write("\n")
          resp = obj.kvs.execute(de_op)
          print(f"resp is {resp}")
          send_msg(conn, resp.encode("utf-8"))
  
        else:
          print(f"no more data")
          break
    finally:
      conn.close()

  def catch_up(self):
    with open("cmd.txt") as f:
      for l in f:
        self.kvs.execute(l.strip())
