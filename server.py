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

  def dest_addr(self):
    other_servers = {k: v for (k, v) in config.server_nodes().items() if k != self.name}
    return list(other_servers.values())

  def start(self):
    server_addr = ('localhost', self.port)
    with open("server_registry.txt", "a") as f:
      f.write(f"{self.name} localhost {self.port}\n")

    print(f"starting up on {server_addr[0]} port {server_addr[1]}")
    print(self.dest_addr())
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_addr)

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
          resp = obj.kvs.execute(de_op)
          print(f"resp is {resp}")
          send_msg(conn, resp.encode("utf-8"))
  
        else:
          print(f"no more data")
          break
    finally:
      conn.close()
