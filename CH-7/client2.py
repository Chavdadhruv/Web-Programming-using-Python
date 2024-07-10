import socket
# TAKE SERVER NAME AND ADDRESS
host = '192.168.107.130'
port = 9000
#CREATE CLIENT SIDE SOCKET USING TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#CONNECT SOCKET WITH SERVER AND PORT
s.connect((host,port))
# ENTER DATA AT CLIENT 
str = input("Enter data - ")
# REPEAT AS LONG AS MESSAGE IS NOT exit
while str != 'exit':
   # SEND  DATA FROM CLIENT TO SERVER
    s.send(str.encode())
    # RECEIVE RESPONSE DATA FROM SERVER
    data = s.recv(1024)
    data = data.decode()
    print("From server - " + data)
    # ENTER DATA
    str = input("Enter data - ")
# DISCONNECT SERVER
s.close()
