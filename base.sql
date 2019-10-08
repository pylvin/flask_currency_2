CREATE TABLE currency (
  id SERIAL PRIMARY KEY,
  date DATE,
  create_time TIMESTAMP DEFAULT NOW()
);
