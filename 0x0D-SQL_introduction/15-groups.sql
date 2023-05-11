-- lists the number of records with the same score in table second_table
SELECT `score`, count(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY 'number' Desc;
