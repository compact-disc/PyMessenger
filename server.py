#####################################
# Christopher DeRoche - compact-disc
# Date Created: 10/7/2020
#
# Python messenger server
#####################################

#!/usr/bin/env python3

# import the sockets
import socket

# importing multithreading
from _thread import *
import threading
lock = threading.Lock()

# SQL Connection
# Local server, account, and database created for PyMessenger
import mysql.connector
sql_db = mysql.connector.connect(
		host="db.cdero.com",
		port="3306",
		user="pymessenger",
		password="L6Bw4NdEhkxuZGtX",
		database="pymessenger"
)

# Server Port
PORT = 800

# Client Connections
clients = []

# Write users username and message to the messages database
def write_message_to_db(usr, msg):
	db_cursor = sql_db.cursor()
	query = "INSERT INTO messages (username, message) VALUES (%s, %s)"
	values = (usr, msg)
	db_cursor.execute(query, values)
	sql_db.commit()

# Echo replies from 1 client to all the connected clients
def echo_replies(msg, conn, username):
	for connection in clients:
		if conn != connection:
			reply = username + ": " + msg
			connection.send(reply.encode())

# Server Class
class Server:
	def start_server():

		# Try and create the socket on PORT
		try:
			# Setup a TCP server on the local machine on port 800
			# Set socket options to be able to reuse port when killing server
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			server.bind(("localhost", PORT))
			print("Server started...")

		# Catch if the socket cannot be created, likely the PORT is in use
		except:
			print("Cannot start the server on port", PORT)

		# Server start listening for connections
		server.listen()

		# Keep a while loop going forever to accept new connections
		while True:
			# Wait for a new connection, then continue
			conn, addr = server.accept()

			# Create a connection variable and add it to the clients array
			client = conn
			clients.append(client)

			#Create a new client class and start it on a new thread
			client_connection = ClientConnection
			start_new_thread(client_connection.connect_client, (conn, addr))

		# Close the server when the loop breaks
		s.close()

# Class for client connections
class ClientConnection:

	# Username for the client
	username = ""

	def connect_client(conn, addr):

		# Get the username and store it as a class variable
		u = conn.recv(255)
		username = u.decode()

		print(username, "connected from", addr)

		# Loop forever as long as there is a client connected
		while True:

			# Receive new data from the client
			data = conn.recv(255)

			# Check if the message is exit
			# If "exit" received, then close the connection and break the loop
			if data.decode() == "exit":
				print(username, "disconnected from", addr)
				conn.close()
				break
			elif len(data.decode()) == 0:
				print(username, "disconnected from", addr)
				conn.close()
				break

			# Otherwise receive the data and print the data, send reply
			else:
				print("Message:", data.decode(), ", from", username, "at", addr)

				write_message_to_db(username, data.decode())
				echo_replies(data.decode(), conn, username)

# Main to start the server
def main():
	print("Starting server...")

	server = Server
	server.start_server()


if __name__ == "__main__":
	main()
