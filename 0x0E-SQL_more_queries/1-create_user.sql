-- Create the MySQL server user user_0d_1
CREATE OR REPLACE USER user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
