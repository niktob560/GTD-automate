CREATE TABLE users (
  name TEXT NOT NULL,
  password VARCHAR(1024) NOT NULL,
  salt VARCHAR(32) NOT NULL,
  email VARCHAR(200) PRIMARY KEY,
  birthday_date DATE NOT NULL,
  mobile_phone TEXT NOT NULL,
  position TEXT NOT NULL
);
