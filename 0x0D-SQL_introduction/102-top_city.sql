-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures
WHERE `month` >= 7 AND `month` <= 8
GROUP BY city
ORDER BY AVG(value) Desc
LIMIT 3;
