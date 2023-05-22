-- 코드를 입력하세요
SELECT 
    PRODUCT_CODE, 
    SALES_AMOUNT*price as SALES
FROM PRODUCT pr
JOIN (
    SELECT 
        PRODUCT_ID,
        sum(SALES_AMOUNT) as SALES_AMOUNT
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
) os
ON pr.PRODUCT_ID = os.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE