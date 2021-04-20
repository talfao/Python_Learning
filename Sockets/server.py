import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server_address = ("127.0.0.1",10000)
print("[+] Server IP {} | Port {}".format(server_address[0],server_address[1]))

sock.bind(server_address)

sock.listen(1)

while True:
    print("[+] Waiting for client connection")
    connection, client_address = sock.accept()

    try:
        print("[+] Connection from", client_address)

        while True:
            data = connection.recv(16)
            print("We recieved", data)
            if data:
                print("Sending back to the client")
                connection.sendall(data)
            else:
                print("No more data from", client_address)
                break
    finally:
        connection.close()
