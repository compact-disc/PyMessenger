-- Create the pymessenger user to access the MariaDB Server
CREATE USER 'pymessenger'@'%' IDENTIFIED BY 'L6Bw4NdEhkxuZGtX';

-- Create a database for PyMessenger and use it
CREATE DATABASE pymessenger;
use pymessenger;

/*
Create a table for messages.
id:		Unsigned Integer, Not Null, Auto_Increment, and Primary Key
username:	Length 16 varchar to store usernames
message:	Length 255 varchar to store messages
*/
CREATE TABLE messages (
	id		INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username	VARCHAR(16),
	message		VARCHAR(255)
);

-- Grant all permissions on pymessager database for the pymessenger user
GRANT ALL ON pymessenger.* TO 'pymessenger'@'%';
