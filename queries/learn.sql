-- CREATE TABLE FOR USERS
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    job TEXT NOT NULL,
    years_experience INT NOT NULL
);

-- ADD email AND is_active COLUMNS
ALTER TABLE users
ADD COLUMN email TEXT
ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

-- UPDATE is_active CASE
UPDATE users
SET is_active = CASE
    WHEN random() > 0.3 THEN TRUE
    ELSE FALSE
END;

SELECT * FROM users;

-- UPDATE AND email DATA WITH FUNCTIONS
UPDATE users
SET email = LOWER(REPLACE(name, ' ', '.')) || '@example.com';

-- CREATE ANALYZE WITH INDEXES
-- ---
-- CREATE UNIQUE INDEX idx_users_email ON users(email);
-- EXPLAIN ANALYZE
-- SELECT * FROM users WHERE email = 'angel@example.com';


-- CREATE ANALYZE WITH INDEXES 
-- CREATE UNIQUE INDEX idx_users_active
-- ON users(id)
-- WHERE is_active = true;

-- EXPLAIN ANALYZE
-- SELECT * FROM users ;


SELECT COUNT(*) FROM users;

SELECT 
	job,
	AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, birth_date))
	) AS avg_age
FROM users 
GROUP BY job
ORDER BY avg_age DESC;

EXPLAIN ANALYZE
SELECT * FROM users
WHERE job = 'Engineer, site'
AND years_experience >= 4;




SELECT * FROM users WHERE birth_date < '1995-01-01';

-- CREATE INDEX idx_users_birthdate
-- ON users(birth_date);

EXPLAIN ANALYZE
SELECT * FROM users
WHERE birth_date < '1995-01-01';


BEGIN;

INSERT INTO users (name, birth_date, job, years_experience, email)
VALUES ('Sara', '1995-03-10', 'Data Scientist', 4, 's@mail.com');

UPDATE users
SET is_active = true
WHERE email = 's@mail.com';

COMMIT;


SELECT * FROM users
WHERE email = 'oar06g@gmail.com';

-- GET LATEST USERS ADDED
SELECT *
FROM (
    SELECT *
    FROM users
    ORDER BY id DESC
    LIMIT 3
) t
ORDER BY id ASC;
