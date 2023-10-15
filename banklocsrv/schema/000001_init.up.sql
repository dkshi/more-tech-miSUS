CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE atms
(
    id SERIAL PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    latitude NUMERIC NOT NULL,
    longitude NUMERIC NOT NULL,
    all_day BOOLEAN NOT NULL
);

CREATE TABLE atms_services
(
    id SERIAL PRIMARY KEY,
    atm_id INT NOT NULL,
    wheelchair_cap BOOLEAN,
    wheelchair_act BOOLEAN,
    blind_cap BOOLEAN,
    blind_act BOOLEAN,
    nfc_cap BOOLEAN,
    nfc_act BOOLEAN,
    qr_cap BOOLEAN,
    qr_act BOOLEAN,
    usd_cap BOOLEAN,
    usd_act BOOLEAN,
    chargerub_cap BOOLEAN,
    chargerub_act BOOLEAN,
    eur_cap BOOLEAN,
    eur_act BOOLEAN,
    rub_cap BOOLEAN,
    rub_act BOOLEAN,
    FOREIGN KEY (atm_id) REFERENCES atms(id)
);

CREATE TABLE atms_load
(
    id SERIAL PRIMARY KEY,
    atm_id INT NOT NULL,
    load INT NOT NULL,
    FOREIGN KEY (atm_id) REFERENCES atms(id)
);

CREATE TABLE offices
(
    id SERIAL PRIMARY KEY,
    salepoint_name VARCHAR(255),
    address VARCHAR(255),
    rko BOOLEAN,
    office_type VARCHAR(255),
    salepoint_format VARCHAR(255),
    suo_availability BOOLEAN,
    has_ramp BOOLEAN,
    latitude DECIMAL NOT NULL,
    longitude DECIMAL NOT NULL,
    metro_station VARCHAR(255),
    distance INT,
    kep BOOLEAN,
    my_branch BOOLEAN
);

CREATE TABLE offices_hours
(
    id SERIAL PRIMARY KEY,
    office_id INT NOT NULL,
    monday VARCHAR(63) NOT NULL,
    tuesday VARCHAR(63) NOT NULL,
    wednesday VARCHAR(63) NOT NULL,
    thursday VARCHAR(63) NOT NULL,
    friday VARCHAR(63) NOT NULL,
    saturday VARCHAR(63) NOT NULL,
    sunday VARCHAR(63) NOT NULL,
    FOREIGN KEY (office_id) REFERENCES offices(id)
);

CREATE TABLE offices_hours_individual
(
    id SERIAL PRIMARY KEY,
    office_id INT NOT NULL,
    monday VARCHAR(63) NOT NULL,
    tuesday VARCHAR(63) NOT NULL,
    wednesday VARCHAR(63) NOT NULL,
    thursday VARCHAR(63) NOT NULL,
    friday VARCHAR(63) NOT NULL,
    saturday VARCHAR(63) NOT NULL,
    sunday VARCHAR(63) NOT NULL,
    FOREIGN KEY (office_id) REFERENCES offices(id)
);

CREATE TABLE hours_predict
(
    id SERIAL PRIMARY KEY,
    office_id INT NOT NULL,
    monday INTEGER[] NOT NULL,
    tuesday INTEGER[] NOT NULL,
    wednesday INTEGER[] NOT NULL,
    thursday INTEGER[] NOT NULL,
    friday INTEGER[] NOT NULL,
    saturday INTEGER[] NOT NULL,
    sunday INTEGER[] NOT NULL,
    FOREIGN KEY (office_id) REFERENCES offices(id)
);

CREATE TABLE hours_individual_predict
(
    id SERIAL PRIMARY KEY,
    office_id INT NOT NULL,
    monday INTEGER[] NOT NULL,
    tuesday INTEGER[] NOT NULL,
    wednesday INTEGER[] NOT NULL,
    thursday INTEGER[] NOT NULL,
    friday INTEGER[] NOT NULL,
    saturday INTEGER[] NOT NULL,
    sunday INTEGER[] NOT NULL,
    FOREIGN KEY (office_id) REFERENCES offices(id)
);

CREATE TABLE offices_load
(
    id SERIAL PRIMARY KEY,
    office_id INT NOT NULL,
    load INT NOT NULL,
    FOREIGN KEY (office_id) REFERENCES offices(id)
);