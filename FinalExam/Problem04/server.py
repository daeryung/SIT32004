import socket
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data.decode('ascii') == "what is your name?":
                print("Received what is your name")
                print("Send my name")
                conn.sendall(b'My name is OOO')
            elif data.decode('ascii') == "How old are you?":
                print("Received how old are you")
                print("Send my age")
                conn.sendall(b'I am 22')
                time.sleep(1)
                conn.sendall(b'Would you want to eat something?')
            elif data.decode('ascii') == "Yes":
                print("Received how old are you")
                print("Send my age")
            elif data.decode('ascii') == 'Sorry, what did you say?':
                print("Get Sorry")
                conn.sendall(b'Would you want to eat something?')
            else:
                print(data.decode('ascii'))
                break