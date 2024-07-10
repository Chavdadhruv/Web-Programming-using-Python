import socket
#SERVER NAME AND ADDRESS
host = 'localhost'
port = 5000
#CREATE SERVER SIDE SOCKET USING TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#BIND SOCKET WITH SERVER AND PORT
s.bind((host,port))
#ALLOW MAX ONE CONNECTION TO THE SOCKET
s.listen(1)
# WAIT TILL CLIENT ACCEPTS CONNECTION
c,addr = s.accept()
# DISPLAY CLIENT ADDRESS
print("connection established from - ", str(addr))
# SEND ENCODED MESSAGE TO CLIENT
c.send(b"Hello client, How are you?")
msg = 'bye'
c.send(msg.encode())
# DISCONNECT SERVER
c.close()
