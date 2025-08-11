CREATE DATABASE pinterest_app;

USE pinterest_app;

-- Users Table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role ENUM('buyer','seller') NOT NULL
);

ALTER TABLE users CHANGE COLUMN name username VARCHAR(100) NOT NULL;


-- Pins Table
CREATE TABLE pins (
    id INT PRIMARY KEY AUTO_INCREMENT,
    seller_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    image_path VARCHAR(255),
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (seller_id) REFERENCES users(id) ON DELETE CASCADE
);

drop table pins;


-- Orders Table
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_id INT NOT NULL,
    pin_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buyer_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (pin_id) REFERENCES pins(id) ON DELETE CASCADE
);


select *from users;

select *from pins;

select *from orders;


describe pins;


ALTER TABLE pins 
ADD COLUMN image_path VARCHAR(255);



SELECT DATABASE();   -- This will show the current database your connection is using
DESCRIBE pins;  


delete from users where id=4;

delete from pins where id=6;