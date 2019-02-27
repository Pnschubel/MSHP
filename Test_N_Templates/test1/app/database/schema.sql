--Payton Schubel
--Automotive Web Dev
--Student Template
--Template of a database schema for reference

--A few notes:
    --ID's are used to identify element of the table. Each section of data has an id.
    --You can't nest tables, but you can use parent-child tables where one element of child is id of parent.
    --Kids can find parents, not vice versa, so we'll have to work backwards.
    
CREATE TABLE customers(
    customerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    customerName TEXT NOT NULL,
    customerEmail TEXT NOT NULL
    );

CREATE TABLE vehicles(
    vehicleId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    make TEXT,
    model TEXT,
    vin TEXT CHECK(vin is null or length(vin) == 14),
    customerId INT NOT NULL,
    FOREIGN KEY(customerId) REFERENCES customers(customerId)
    );

CREATE TABLE repairs(
    repairId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    repairType TEXT NOT NULL,
    accepted BOOLEAN,
    vehicleId INT NOT NULL,
    FOREIGN KEY(vehicleId) REFERENCES vehicles(vehicleId)
    );
