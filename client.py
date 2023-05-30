import socket
Server_ip="192.168.56.1"
Server_host=8002
FORMAT="utf-8"
CS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
CS.connect((Server_ip,Server_host))
file = open("check.txt","r")
data=file.read()
CS.send("check.txt".encode(FORMAT))
msg=CS.recv(1024)
print( msg)
CS.send(data.encode(FORMAT))
msg=CS.recv(1024)
print(msg)
