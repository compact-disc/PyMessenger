#####################################
# Christopher DeRoche - compact-disc
# Date Created: 10/7/2020
#
# Python messenger client
#####################################

#!/usr/bin/env python3

import socket

class Client:
	def connect_client():
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect(("localhost", 800))

		while True:
			msg = input()

			if msg == "disconnect":
				client.sendall(msg.encode())
				data = client.recv(512)
				print(data.decode())
				client.close()
				break
			elif msg == "shutdown":
				client.sendall(msg.encode())
				data = client.recv(512)
				print(data.decode())
				client.close()
				break
			else:
				client.sendall(msg.encode())
				data = client.recv(512)
				print(data.decode())


def main():
	client = Client
	client.connect_client()

if __name__ == "__main__":
	main()
