CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    email TEXT NOT NULL UNIQUE
    cart_id INT
    created_at DATETIME
    updated_at DATETIME
);
