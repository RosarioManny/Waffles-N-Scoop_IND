CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    cart_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cart_id) REFERENCES cart(id)
);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    image TEXT NOT NULL,
    price INT NOT NULL,
    quantity INT,
    description TEXT,
    category TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    total INT NOT NULL,
    user_id INTEGER,
    created_at DATETIME  DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

INSERT INTO items (name, image, price, quantity, description, category, updated_at) VALUES
('Birthday Cake Confetti', 'birthday_cake_confetti.jpg', 15, 120, 'Colorful confetti cake flavor for celebrations!','ice-cream', datetime('now')),
('Chocolate Moose', 'chocolate_moose.jpg', 11, 200, 'Rich and creamy chocolate ice cream.','ice-cream', datetime('now')),
('French Cinnamon Vanilla', 'french_cinnamon_vanilla.jpg', 11, 150, 'A French twist on classic vanilla with a hint of cinnamon.','ice-cream', datetime('now')),
('Matcha Pistachio', 'matcha_pistachio.jpg', 15, 100, 'A unique blend of matcha green tea and roasted pistachio.','ice-cream', datetime('now')),
('Cookies''N''Cream', 'cookies_n_cream.jpg', 13, 250, 'Classic cookies and cream flavor with crunchy cookie bits.','ice-cream', datetime('now')),
('Classic Sweet Strawberry', 'classic_sweet_strawberry.jpg', 111, 80, 'Sweet and tangy strawberry ice cream made with real strawberries.','ice-cream', datetime('now')),
('Raspberry Sorbet', 'raspberry_sorbet.jpg', 13, 180, 'Refreshing raspberry sorbet, perfect for a light treat.','ice-cream', datetime('now')),
('Black Currant Sorbet', 'black_currant_sorbet.jpg', 13, 170, 'Tart and tangy black currant sorbet.','ice-cream', datetime('now')),
('Coffee Javachip', 'coffee_javachip.jpg', 15, 140, 'Bold coffee flavor with rich chocolate chips.','ice-cream', datetime('now')),
('Cotton Candy Blitz', 'cotton_candy_blitz.jpg', 13, 160, 'Fun and whimsical cotton candy flavor.','ice-cream', datetime('now')),
('Original Waffle Cones (4 Pack)', 'waffle_cone_4pack.jpg', 15, 300, 'A pack of 4 crispy, original waffle cones.', 'food', datetime('now')),
('Sugar Cones (8 Pack)', 'sugar_cones_8pack.jpg', 9, 300, 'A pack of 8 classic sugar cones.', 'food', datetime('now')),
('Original Waffle Bowls (2 Pack)', 'waffle_bowls_2pack.jpg', 12, 250, 'A pack of 2 original waffle bowls.', 'food', datetime('now')),
('Waffle''N''Scoop Tote', 'waffle_scoop_tote.jpg', 20, 100, 'Stylish tote bag for carrying your ice cream essentials.', 'merchandise', datetime('now')),
('Waffle''N''Scoop Hat', 'waffle_scoop_hat.jpg', 20, 90, 'Comfortable hat with the Waffle''N''Scoop logo.', 'merchandise', datetime('now')),
('Waffle''N''Scoop T-Shirt', 'waffle_scoop_tshirt.jpg', 30, 70, 'Soft and stylish t-shirt featuring the Waffle''N''Scoop brand.', 'merchandise', datetime('now'));