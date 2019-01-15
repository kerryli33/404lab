#!/usr/bin/env python3
import socket

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def conn_socket(addr_tup):
	(family,socktype,proto,canonname,sockaddr) = addr_tup
	try:
		s = socket.socket(family,socktype,proto)	#create socket
		s.connect(sockaddr)	#connect to socket
		s.sendall(payload.encode())	#send payload 

		full_data = b""
		while True:	
			data = s.recv(BUFFER_SIZE)
			if not data:
				break
			full_data += data
		print(full_data)

	except e:
		print(e)
		pass
	finally:
		s.close()
def main():
	addr_info = socket.getaddrinfo(HOST,PORT,proto=socket.SOL_TCP)
	#print(addr_info)
	for addr_tup in addr_info:
		#Destructure the socket returned tuple
		print(addr_tup)
		conn_socket(addr_tup)
		#only IPV4
		break

if __name__ == "__main__":
	main()
