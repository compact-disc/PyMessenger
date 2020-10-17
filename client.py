#####################################
# Christopher DeRoche - compact-disc
# Date Created: 10/7/2020
#
# Python messenger client
#####################################

#!/usr/bin/env python3

# import sockets
import socket

# import the argument parser
import argparse

class Client:
	def connect_client(username):
		
		# Try and connect to the server
		try:
			# Create the TCP connection on port 800 to the server
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect(("localhost", 800))
			print("Connected to server...")

		# Catch if cannot connect to the server and exit (server likely not running)
		except:
			print("Cannot connect to server, exiting...");
			exit()

		# Send the username to the server first
		client.sendall(username.encode())

		# Keep waiting for new input until connection closed
		while True:

			# Get the user input
			msg = input(str(">>"))

			# If the input is exit, then send message, receive, close and break
			if msg == "exit":
				client.sendall(msg.encode())
				data = client.recv(255)
				print("Disconnected...")
				client.close()
				break

			# Else receive and print the response
			else:
				client.sendall(msg.encode())
				data = client.recv(255)
				print(data.decode())


def main():

	# Create the argument parser for PyMessenger and name it
	parser = argparse.ArgumentParser(description="PyMessenger")

	# Add the username argument for the clients, default can be set at DUser
	parser.add_argument("-u", '--username', type=str, default="DUser", help="Client username")

	# Take in the arguments
	arguments = parser.parse_args()

	# Create the client object and send the username
	client = Client
	client.connect_client(arguments.username)

if __name__ == "__main__":
	main()
