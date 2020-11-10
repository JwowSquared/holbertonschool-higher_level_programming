-- create a table called first_table in the current database
-- this query creates a table with fields id and name
IF NOT EXISTS (CREATE TABLE first_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
name VARCHAR(256));
