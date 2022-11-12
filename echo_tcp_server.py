import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # check if self.data contains string "SECRET"
        out = "Secret not found"
        rec_str = self.data.decode("utf-8")
        if "SECRET" in rec_str:
            print("Secret found")
            count = 0
            digits = ""
            for char in rec_str:
                if (char.isdigit()):
                    count += 1
                    digits += char
            out = "Digits: " + digits + " Count: " + str(count)
        self.request.sendall(bytes(out + '\n', 'utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9998

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
