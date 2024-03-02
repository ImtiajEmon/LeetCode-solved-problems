# Way - 1
#SELECT max(num) AS num FROM MyNumbers
#WHERE num IN
#(SELECT num
#FROM MyNumbers
#GROUP BY num
#HAVING COUNT(*) = 1);

# Way - 2
WITH cte AS(
    SELECT num FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)

SELECT MAX(num) AS num
FROM cte;
