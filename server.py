#####################################
# Christopher DeRoche - compact-disc
# Date Created: 10/7/2020
#
# Python messenger server
#####################################

#!/usr/bin/env python3

import socket

class Server:
	def start_server():
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(("localhost", 800))
		server.listen()

		while True:

			conn, addr = server.accept()

			print("connection from:", addr)

			while True:
				data = conn.recv(512)
				print("message from", addr)
				if data.decode() == "shutdown":
					conn.close()
					exit()
				elif data.decode() == "disconnect":
					conn.close()
					break
				else:
					reply = data.decode()
					conn.send(reply.encode())

def main():
	server = Server
	server.start_server()


if __name__ == "__main__":
	main()
