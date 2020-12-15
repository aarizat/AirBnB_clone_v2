-- prepares a MySQL server
-- creat hbnb_dev_db database if not exist
-- set new user hbnb_dev (in localhost)
--  set password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have SELECT privilege on the database
-- performance_schema (and only this database)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
