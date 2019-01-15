#!/usr/bin/env python3
import socket
from multiprocessing import Pool


HOST = "localhost"
PORT = 8081
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def conn_socket(addr_tup):
	(family,socktype,proto,canonname,sockaddr) = addr_tup
	print(addr_tup)
	try:
		s = socket.socket(family,socktype,proto)	#create socket
		s.connect(sockaddr)	#connect to socket
		s.sendall(payload.encode())	#send payload 
		
		s.shutdown(socket.SHUT_WR)	#if your code ever hangs and doesn't return anything, try usnig this shutdown method

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
		with Pool() as p:
			#Pool determines the number of "workers" you ahve (?)
			p.map(conn_socket, [addr_tup for _ in range(1,50)]) 
			

		#Destructure the socket returned tuple
		#conn_socket(addr_tup)
		#only IPV4
		break

if __name__ == "__main__":
	main()
