-- py -m venv venv
-- venv\Scripts\activate
-- pip install -r requirements.txt

-- Krijimi i Databazes

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    category VARCHAR(50)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date DATE
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT
);


-- Insert
INSERT INTO customers (name, email) VALUES
('Ardit', 'ardit@test.com'),
('Mira', 'mira@test.com'),
('Luan', 'luan@test.com');

INSERT INTO products (name, price, category) VALUES
('Laptop', 799.99, 'Electronics'),
('Mouse', 19.99, 'Electronics'),
('Headphones', 49.99, 'Electronics'),
('Coffee', 4.99, 'Food'),
('Tea', 3.99, 'Food');

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2024-02-01'),
(1, '2024-02-10'),
(2, '2024-02-12');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),  
(1, 2, 2),  
(2, 4, 3),  
(3, 3, 1);  

-- Kerkesat
-- Shfaq te gjithe klientet
-- Shfaq te gjithe produktet me çmimin > 20€
-- Ndrysho çmimin e “Mouse” ne 25€
--Fshi produktet e kategorise “Food” me çmim < 4€
--Gjej te gjitha porosite me emrin e klientit
--Gjej sa artikuj ka çdo porosi
--Gjej totalin (ne euro) te çdo porosie
--Gjej klientin me me shume porosi
--Shfaq 3 produktet me te shtrenjta
--Gjej totalin e shpenzimeve te klientit “Ardit”
--Numero sa produkte ka ne çdo kategori
--Shfaq klientet qe nuk kane bere asnje porosi
