-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS lv_dev_db;
CREATE USER IF NOT EXISTS 'lv_dev'@'localhost' IDENTIFIED BY 'lv_dev_pwd';
GRANT ALL PRIVILEGES ON `lv_dev_db`.* TO 'lv_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'lv_dev'@'localhost';
FLUSH PRIVILEGES;
