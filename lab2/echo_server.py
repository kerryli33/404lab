#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8081	#low numbers are reserved for OS
BUFFER_SIZE = 1024


def main():
	
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)	#allows addy to be reused
		s.bind((HOST,PORT)) #bind to an addy
		s.listen(1)	#listens for connection
		
		while True:

			conn, addr = s.accept()
			with conn:
				print(conn)
				print("connected by: ", addr)
				full_data = b""
				while True:
					data = conn.recv(BUFFER_SIZE)
					if not  data:
						break
					full_data += data
				#print(full_data)
				conn.sendall(full_data)
						
	
if __name__ == "__main__":
	main()

