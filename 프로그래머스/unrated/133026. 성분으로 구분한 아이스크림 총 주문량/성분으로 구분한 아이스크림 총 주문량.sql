-- 코드를 입력하세요
SELECT 
    INGREDIENT_TYPE, 
    SUM(TOTAL_ORDER) AS TOTAL_ORDER 
FROM FIRST_HALF
JOIN ICECREAM_INFO USING(FLAVOR)
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER