DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS pubs;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    country VARCHAR(255)
    visited BOOLEAN
);

CREATE TABLE pubs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    visited - BOOLEAN
    city_id INT REFERENCES cities(id)
);