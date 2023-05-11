-- computes the score average of all records in the table second_table
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures
GROUP BY city
ORDER BY AVG(value) Desc;
