import socket
# TAKE SERVER NAME AND ADDRESS
host = 'localhost'
port = 5000
#CREATE CLIENT SIDE SOCKET USING TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#CONNECT SOCKET WITH SERVER AND PORT
s.connect((host,port))
# RECEIVE MAX 1024 BYTES MESSAGE FROM SERVER AT A TIME
msg = s.recv(1024)
# REPEAT AS LONG AS MESSAGE IS NOT EMPTY
while msg:
    print("Received - ", msg.decode())
    msg = s.recv(1024)
# DISCONNECT SERVER
s.close()
