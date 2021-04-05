import threading

class KVStore:
  def __init__(self):
    self.lock = threading.Lock()
    self.data = {}

  def get(self, k):
    return self.data.get(k, "nil")

  def set(self, k, v):
    self.data[k] = v

  def delete(self, k):
    del self.data[k]

  def execute(self, op):
    cmd, key = 0, 1
    operands = op.split(" ")

    resp = "Sorry, I don't understand taht command,"

    with self.lock:
      if operands[cmd] == "get":
        resp = self.get(operands[key])
      elif operands[cmd] == "set":
        v = " ".join(operands[2:])
        self.set(operands[key], v)
        resp = f"key {operands[key]} set to {v}"
      elif operands[cmd] == "delete":
        self.delete(operands[key])
        resp = f"key {key} deleted"
      elif operands[cmd] == "show":
        resp = str(self.data)
      else:
        pass
      return resp

