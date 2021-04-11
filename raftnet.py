import queue
import config
import msg
import socket

class SockNetWork:
  def __init__(self):
    self.socks = {}
  
  def send(self, dest, msg):
    if dest not in self.socks:
      self.socks[dest] = socket(AF_INET, SOCK_STREAM)
      self.socks[dest].connect(config.nodes[dest])

def start_recv(self, server):
  threading.Thread(target=self._server, args=(server,), daemon=True).start()

def _server(self, server):
  sock = socket(AF_INET, SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(config.nodes[server.addr])
  sock.listen(1)

  while True:
    client, addr = sock.accept()
    threading.Thread(target=self.get_msg, args=(server, client,), daemon=True).start()

def get_msg(self, server, sock):
  while True:
    m = msg.recv_msg(sock)
    server.inbox.put(msg)

class RaftServer:
  def __init__(self, addr, net):
    self.inbox = queue.Queue()
    self.addr = addr
    self.net = net

  def send(self, dest, msg):
    self.net.send(dest, msg)

  def recv(self):
    return self.inbox.get()
