-- Display the average temperature by city ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;
