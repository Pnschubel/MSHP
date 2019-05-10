--Payton Schubel & Sean Kuderna
--Automotive Web Dev
--Student Template
--Template of a database schema for reference

--A few notes:
    --ID's are used to identify element of the table. Each section of data has an id.
    --You can't nest tables, but you can use parent-child tables where one element of child is id of parent.
    --Kids can find parents, not vice versa, so we'll have to work backwards.

--Pre-Existing Stuff gets added to the tables
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS vehicles;
DROP TABLE IF EXISTS repairs;

CREATE TABLE customers(
    customerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    customerName TEXT NOT NULL,
    customerEmail TEXT NOT NULL,
    customerPhoneNum TEXT 
    );

CREATE TABLE vehicles(
    vehicleId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    make TEXT,
    model TEXT,
    year TEXT,
    vin TEXT CHECK(vin is null or length(vin) == 14),
    vin2 TEXT,
    customerId INT NOT NULL,
    FOREIGN KEY(customerId) REFERENCES customers(customerId)
    );

CREATE TABLE repairs(
    repairId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    repairType TEXT NOT NULL,
    repairDescription TEXT,
    accepted BOOLEAN,
    completed BOOLEAN NOT NULL,
    vehicleId INT NOT NULL,
    FOREIGN KEY(vehicleId) REFERENCES vehicles(vehicleId)
    );

