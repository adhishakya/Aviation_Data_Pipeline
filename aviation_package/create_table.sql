CREATE DATABASE IF NOT EXISTS `aviation_db`;
USE `aviation_db`;

CREATE TABLE IF NOT EXISTS aviation_data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_date DATE,
    flight_status VARCHAR(255),
    departure_airport VARCHAR(255),
    departure_timezone VARCHAR(255),
    departure_scheduled TIMESTAMP,
    departure_estimated TIMESTAMP,
    arrival_airport VARCHAR(255),
    arrival_timezone VARCHAR(255),
    arrival_scheduled TIMESTAMP,
    arrival_estimated TIMESTAMP,
    airline_name VARCHAR(255),
    flight_number VARCHAR(255),
    flight_icao VARCHAR(255)
);
