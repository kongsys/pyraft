nodes = {
  0: ('localhost', 15000),
  1: ('localhost', 15001),
  2: ('localhost', 15002),
  3: ('localhost', 15003),
  4: ('localhost', 15004),
}

def server_nodes():
  registry = {}

  with open("server_registry.txt", "r") as f:
    for l in f:
      cmd = l.strip()
      print(cmd)
      server = cmd.split()
      if len(server) == 3:
        registry[server[0]] = (server[1], server[2])
  return registry

