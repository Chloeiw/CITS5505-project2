CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username CHAR(50) NOT NULL,
    interest INT NOT NULL,
    password CHAR(20) NOT NULL,
    image VARCHAR NOT NULL
);

CREATE TABLE question (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR NOT NULL,
    subtitle VARCHAR NOT NULL,
    content VARCHAR NOT NULL,
    cover VARCHAR NOT NULL,
    post_time CURRENT_TIMESTAMP NOT NULL,
    category_id INT NOT NULL,
    user_id INT NOT NULL
);

CREATE TABLE answer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comment VARCHAR NOT NULL,
    answer_time CURRENT_TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    question_id INT NOT NULL
);

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR NOT NULL
);


ALTER TABLE question(
    ADD post_time CURRENT_TIMESTAMP NOT NULL
);