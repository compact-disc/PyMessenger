# PyMessenger

Python command line messenger with a server and client. Created and tested in Ubuntu Linux.
The server uses MySQL/MariaDB to log messages by username and ID. Client and Server use multithreading to
perform multiple operations concurrently.

### Complete:
- Multiple clients (Multithreading)
- Usernames on clients with argument parsing on the client side
- Added more print messages to server side with useful information about who is sending each message
- Added >> to client for distinguishing between send/receive
- Comments on the code
- Added the ability to just reuse the port if server crashes, close with Control-C (no more "port taken" issue)
- Add MySQL database to store message id, username, and message
- Echo messages to all clients after sending
- Add usernames to replies
- Added Python logging to server

### Todo:
- ~~Multiple Clients (Multithreading)~~
- ~~Usernames on clients~~
- ~~Echo messages to all clients after sending~~
- ~~Add MySQL database to store message id, username, and message~~
- ~~Add usernames to replies~~
- Add server side commands
- More exception handling
- User database with login upon connecting to server with client
- TLS/SSL Encryption between client and server
- Improve logging on server side

