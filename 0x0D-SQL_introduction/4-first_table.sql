-- Check if the table exists before creating it
-- This script will not fail if the table already exists
-- Use the `CREATE TABLE` statement with `IF NOT EXISTS`

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
