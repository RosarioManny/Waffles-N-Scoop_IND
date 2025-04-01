# CS50 Final Project

## Title: Waffles N' Scoop

<img src="./static/images/Product_Photos/Waffle_N_Scoop_logo.png">

## Video DEMO:

## Description:

An ice cream e-commerce website made to give the feel of purchaseing products like ice-cream, ice-cream products and company merchandise.
Users can create an account, browse items, add to carts and checkout.
The purpose for this project is to develop an E-commerce site to practice real world skills. Implement users, sign-in, registration, shopping cart, company feel and endpoints.

## Technologies:

1. Python - Code
1. Javascript - Code
1. Flask - Backend
1. Jinja2 - Templating
1. Pip - Environments
1. Github - Repository and Code Management
1. CSS - Stylizing
1. HTML - Document
1. Render - Deployment
1. VScode - Code Intepreter

## MVP:

- Registration
- Sign-In
- Navigation bar
- Home Page
- About Page
- Shopping Page
- Profile Page
- Cart Page
- Footer

## POST-MVP

- History Page - Unsure if this makes sense for an ice-cream shop.
- Optimizations and improvements - Improved Styles, animation, user-quality of life

## Routes & Endpoints

- "/register" - Registration Page - GET, POST
- "/login" - Sign-In Page - GET, POST
- "/logout" - Logout
- "/" - Home page - GET
- "/about" - About Page - GET
- "/shop" - Shop Page - GET, POST
- "/cart" - Cart Page - GET, POST
  "/cart/remove" - Remove Item from cart - POST
- "/checkout" - POST
- "/profile" - Profile Page - GET
- "/edit-profile" - GET, POST

## Models

### Users

```
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
```

### Items

```
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
```

### Cart

```
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
```

### Cart Items

```
CREATE TABLE IF NOT EXISTS cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER,          -- Links to `cart.id`
    product_id INTEGER,       -- Links to `products.id`
    quantity INTEGER,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cart_id) REFERENCES cart(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### Orders

```
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    order_total DECIMAL(10, 2),
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Order Items

```
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## Design

Inspiration for the website was from the colors of classic ice-creams, Chocolate, Strawberry and Vanilla.
I use blue as a highlight areas of importance or that I want guest to look at.

### Color Scheme:

Vanilla : Used for backgrounds and input fields

- ![#FFFFF6](https://placehold.co/15x15/FFFFF6/FFFFF6.png) `#FFFFF6`
- ![#FFF5E2](https://placehold.co/15x15/FFF5E2/FFF5E2.png) `#FFF5E2`
- ![#E7D8BA](https://placehold.co/15x15/E7D8BA/E7D8BA.png) `#E7D8BA`
  
Blue Raspberry: Used for call-to-actions, highlights, hovers and other accents of the site.

<span style="background-color: #38DDFF; display: inline-block; width: 1.5rem; height: 1rem; border-radius: 2px"></span> &rarr; #38DDFF

<span style="background-color: #DAFFFF; display: inline-block; width: 1.5rem; height: 1rem; border-radius: 2px"></span> &rarr; #DAFFFF
- ![#38DDFF](https://placehold.co/15x15/38DDFF/38DDFF.png) `#38DDFF`
- ![#DAFFFF](https://placehold.co/15x15/DAFFFF/DAFFFF.png) `#DAFFFF`
- 
Strawbery: Used as the main drive for color. Highlighting titles, links, buttons, important informaion and more.

<span style="background-color: #FFDFF1; display: inline-block; width: 1.5rem; height: 1rem; border-radius: 2px"></span> &rarr; #FFDFF1

<span style="background-color: #FF8DB5; display: inline-block; width: 1.5rem; height: 1rem; border-radius: 2px"></span> &rarr; #FF8DB5
- ![#FF8DB5](https://placehold.co/15x15/FF8DB5/FF8DB5.png) `#FF8DB5`
- ![#FFDFF1](https://placehold.co/15x15/FFDFF1/FFDFF1.png) `#FFDFF1`
- 
Chocolate: It's dark color was great for fonts and regular text.

<span style="background-color: #332100; display: inline-block; width: 1.5rem; height: 1rem; border-radius: 2px"></span> &rarr; #332100

<span style="background-color: #553E13; display: inline-block; width: 1.5rem; height: 1rem; border-radius: 2px"></span> &rarr; #553E13
- ![#332100](https://placehold.co/15x15/332100/332100.png) `#332100`
- ![#553E13](https://placehold.co/15x15/553E13/553E13.png) `#553E13`

## Set-up

1. Fork and clone Git

1. Install flask and sqlite3

```
pip install flask sqlite3
```

1. Run Schema file

```
sqlite3 database.db
```

## User Flow

1. Users lands on home page. Viewing the newsest deal, customer photos and encouraged to visit the shop

1. Explore "About" page and learn about the company owner, location and customer photos

1. Login or Create account an account to shop

1. Browse shop for ice-cream flavors, merchandise or ice-cream products.

1. Choose the amount you want and add to cart

1. View cart and remove unwanted items.

1. If finished browsing and adding to cart, Purchase.
