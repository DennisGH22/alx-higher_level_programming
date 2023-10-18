-- Create the MySQL server user user_0d_1
CREATE IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
