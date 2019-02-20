--Payton Schubel
--Automotive Web Dev
--Student Template
--Template of a database schema for reference

--A few notes:
    --ID's are used to identify element of the table. Each section of data has an id.
    --You can't nest tables, but you can use parent-child tables where one element of child is id of parent.
    --Kids can find parents, not vice versa, so we'll have to work backwards.
    
CREATE TABLE customer(
    id INTEGER PRIMARY KEY,
    customer-name TEXT NOT NULL,
    customer-email TEXT NOT NULL
    );

CREATE TABLE vehicle(
    id INTEGER PRIMARY KEY,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    vin INTEGER,
    customer-id INTEGER NOT NULL
    );

CREATE TABLE repairs(
    id INTEGER PRIMARY KEY,
    repair-type TEXT NOT NULL,
    accepted BOOLEAN NOT NULL,
    vehicle-id INTEGER
    );
