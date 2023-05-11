-- creates a table second_table in hbtn_0c_0 db if it doesn't exists
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);
-- add multiples rows into second_name
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
