import socket
import sys

HOST, PORT = "10.10.10.2", 9997
file = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    f = open("in.txt", "r")
    for line in f:
        sock.send(bytes(line, "utf-8"))
    f.close()
