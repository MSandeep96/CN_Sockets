import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Receiving file from: {}".format(self.client_address[0]))
        f = open("out.txt", "w")
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                break
            f.write(self.data.decode("utf-8"))
        f.close()
        print("File received and saved to out.txt")


if __name__ == "__main__":
    HOST, PORT = "localhost", 9998

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
