-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS lv_test_db;
CREATE USER IF NOT EXISTS 'lv_test'@'localhost' IDENTIFIED BY 'lv_test_pwd';
GRANT ALL PRIVILEGES ON `lv_test_db`.* TO 'lv_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'lv_test'@'localhost';
FLUSH PRIVILEGES;
