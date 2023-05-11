-- lists all records of the table second_table
SELECT score, name FROM second_table
-- filters null `name`
WHERE name IS NOT NULL
ORDER BY score Desc;
