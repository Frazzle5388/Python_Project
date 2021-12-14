DROP TABLE IF EXISTS pubs;
DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE pubs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_id INT REFERENCES cities(id),
    visited BOOLEAN
);