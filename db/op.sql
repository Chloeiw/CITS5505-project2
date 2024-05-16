CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username CHAR(50) NOT NULL,
    password CHAR(20) NOT NULL,
    image VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR NOT NULL,
    subtitle VARCHAR NOT NULL,
    content VARCHAR NOT NULL,
    cover VARCHAR NOT NULL,
    post_time CURRENT_TIMESTAMP NOT NULL,
    category_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS answer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment VARCHAR NOT NULL,
    answer_time CURRENT_TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (question_id) REFERENCES question(id)
);

CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL
);


CREATE TABLE IF NOT EXISTS userInterest (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);