
--InventoryItem table
CREATE TABLE InventoryItem (
    id SERIAL PRIMARY KEY,
    Item_SKU VARCHAR(50) UNIQUE NOT NULL,
    Item_Name VARCHAR(100) NOT NULL,
    Item_Description TEXT,
    Item_Price NUMERIC(10, 2) NOT NULL,
    Item_Qty INT NOT NULL
);

--Customer table
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    c_name VARCHAR(100) NOT NULL,
    c_email VARCHAR(120) UNIQUE NOT NULL,
    c_contact VARCHAR(20)
);

--Staff table
CREATE TABLE Staff (
    id SERIAL PRIMARY KEY,
    s_name VARCHAR(100) NOT NULL,
    s_email VARCHAR(120) UNIQUE NOT NULL,
    s_isAdmin BOOLEAN DEFAULT FALSE,
    s_contact VARCHAR(20)
);

--Transaction table
CREATE TABLE Transaction (
    id SERIAL PRIMARY KEY,
    c_ID INT NOT NULL,
    s_ID INT NOT NULL,
    Item_ID INT NOT NULL,
    t_date DATE NOT NULL,
    t_amount NUMERIC(10, 2) NOT NULL,
    t_category VARCHAR(50),
    FOREIGN KEY (c_ID) REFERENCES Customer(id),
    FOREIGN KEY (s_ID) REFERENCES Staff(id),
    FOREIGN KEY (Item_ID) REFERENCES InventoryItem(id)
);
