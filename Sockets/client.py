import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server_address = ("127.0.0.1",10000)
print("[+] We are connecting to the server {} on port {}".format(server_address[0],server_address[1]))
sock.connect(server_address)


try:
    message = "Hello, some words." 
    print("Sending this message \'{}\' to server.".format(message))
    sock.sendall(bytes(message, "utf-8"))

    amount_recieved = 0
    amount_expected = len(message)

    while amount_recieved < amount_expected:
        data = sock.recv(16)
        amount_recieved += len(data)
        print("[+] Recieved", data)

finally:
    sock.close()
