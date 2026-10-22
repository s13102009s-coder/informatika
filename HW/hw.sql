
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    balance REAL DEFAULT 0.0,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    sale INTEGER DEFAULT 0, 
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users (name, email, balance) VALUES 
('Иван Иванов', 'ivan@example.com', 1500.50),
('Мария Петрова', 'maria@example.com', 2300.00),
('Алексей Смирнов', 'alex@example.com', 500.00);


INSERT INTO products (name, price, sale) VALUES 
('Ноутбук', 75000.00, 10),
('Смартфон', 45000.00, 5),
('Наушники', 5000.00, 0),
('Клавиатура', 3500.00, 15);


SELECT * FROM users;
SELECT * FROM products;
