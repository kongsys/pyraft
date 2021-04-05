import socket
import threading
from store import KVStore
from msg import *

def upup(s):
  with open("cmd.txt") as f:
    for l in f:
      s.execute(l.strip())

def run_server():
  kvs = KVStore()
  upup(kvs)
  server_address = ("localhost", 10000)
  print(f"starting up on {server_address[0]} port {server_address[1]}")

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(server_address)

  sock.listen(1)

  while True:
    conn, addr = sock.accept()

    print(f"connection from {addr}")
    threading.Thread(target=handle_conn, args=(conn, kvs)).start()

def handle_conn(conn, kvs):
  try:

    while True:
      op = recv_msg(conn)
      if op:
        de_op = op.decode("utf-8")
        print(f"received {de_op}")
        with open("cmd.txt", "a") as f:
          f.write(de_op)
          f.write("\n")
        resp = kvs.execute(de_op)
        print(f"resp is {resp}")
        send_msg(conn, resp.encode("utf-8"))

      else:
        print(f"no more data")
        break
  finally:
    conn.close()

run_server()
