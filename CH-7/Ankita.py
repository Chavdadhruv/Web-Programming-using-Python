import socket
#SERVER NAME AND ADDRESS
host = '0.0.0.0'
port = 9000
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
# RUN SERVER CONTINUOUSLY
while True:
    data = c.recv(1024)
    #IF CLIENT SENDS EMPTY STRING, COME OUT OF WHILE LOOP
    if not data:
        break
    print("From client - " + str(data.decode()))
    # ENTER RESPONSE FROM SERVER
    data1 = input("Enter the response = ")
    # SEND THAT DATA TO CLIENT
    c.send(data1.encode())
# DISCONNECT SERVER
c.close()
