CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    name TEXT, 
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    description TEXT,
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
('Birthday Cake Confetti', '/Birthday_cake.jpeg', 15, 120, 'Colorful confetti cake flavor for celebrations!','ice_cream', datetime('now')),
('Chocolate Moose', '/Chocolate-Moose.jpeg', 11, 200, 'Rich and creamy chocolate ice cream.','ice_cream', datetime('now')),
('French Cinnamon Vanilla', '/French-Cinnamon-Vanilla.jpeg', 11, 150, 'A French twist on classic vanilla with a hint of cinnamon.','ice_cream', datetime('now')),
('Matcha Pistachio', '/Matcha-Pistachio.jpeg', 15, 100, 'A unique blend of matcha green tea and roasted pistachio.','ice_cream', datetime('now')),
('Cookies''N''Cream', '/Cookies-N-Cream.jpeg', 13, 250, 'Classic cookies and cream flavor with crunchy cookie bits.','ice_cream', datetime('now')),
('Classic Sweet Strawberry', '/Classic-Strawberry.jpeg', 111, 80, 'Sweet and tangy strawberry ice cream made with real strawberries.','ice_cream', datetime('now')),
('Raspberry Sorbet', '/Raspberry-Sorbet.jpeg', 13, 180, 'Refreshing raspberry sorbet, perfect for a light treat.','ice_cream', datetime('now')),
('Black Currant Sorbet', '/Black-currant-Sorbet.jpeg', 13, 170, 'Tart and tangy black currant sorbet.','ice_cream', datetime('now')),
('Coffee Javachip', '/Coffee-Javachip.jpeg', 15, 140, 'Bold coffee flavor with rich chocolate chips.','ice_cream', datetime('now')),
('Cotton Candy Blitz', '/Cotton-Candy-Blitz.jpeg', 13, 160, 'Fun and whimsical cotton candy flavor.','ice_cream', datetime('now')),
('Original Waffle Cones (4 Pack)', 'waffle_cone_4pack.jpg', 15, 300, 'A pack of 4 crispy, original waffle cones.', 'food', datetime('now')),
('Sugar Cones (8 Pack)', 'sugar_cones_8pack.jpg', 9, 300, 'A pack of 8 classic sugar cones.', 'food', datetime('now')),
('Original Waffle Bowls (2 Pack)', 'waffle_bowls_2pack.jpg', 12, 250, 'A pack of 2 original waffle bowls.', 'food', datetime('now')),
('Waffle''N''Scoop Tote', 'waffle_scoop_tote.jpg', 20, 100, 'Stylish tote bag for carrying your ice cream essentials.', 'merchandise', datetime('now')),
('Waffle''N''Scoop Hat', 'waffle_scoop_hat.jpg', 20, 90, 'Comfortable hat with the Waffle''N''Scoop logo.', 'merchandise', datetime('now')),
('Waffle''N''Scoop T-Shirt', 'waffle_scoop_tshirt.jpg', 30, 70, 'Soft and stylish t-shirt featuring the Waffle''N''Scoop brand.', 'merchandise', datetime('now'));