-- 코드를 입력하세요
SELECT 
    FO.PRODUCT_ID, 
    PRODUCT_NAME,
    SUM(PRICE*AMOUNT) AS TOTAL_SALES
FROM FOOD_ORDER FO
JOIN FOOD_PRODUCT FR
ON FO.PRODUCT_ID = FR.PRODUCT_ID
WHERE DATE_FORMAT(PRODUCE_DATE,'%Y-%m') = '2022-05'
GROUP BY PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC