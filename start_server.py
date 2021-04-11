import sys

from server import Server

Server(name="Server1", port=int(sys.argv[1])).start()
