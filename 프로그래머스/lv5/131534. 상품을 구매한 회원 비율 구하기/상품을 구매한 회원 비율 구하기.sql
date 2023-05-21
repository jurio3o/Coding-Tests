WITH user AS
    (
    SELECT 
        user_id 
    FROM USER_INFO
    WHERE EXTRACT(YEAR FROM JOINED) = 2021
    )

,tb AS(
    SELECT
        EXTRACT(YEAR FROM SALES_DATE) AS YEAR, 
        EXTRACT(MONTH FROM SALES_DATE) AS MONTH, 
        count(distinct os.user_id) as buying_user_cnt
    FROM ONLINE_SALE as os
    JOIN user
    ON os.user_id = user.user_id
    GROUP BY YEAR, MONTH
)
SELECT 
    YEAR,
    MONTH,
    buying_user_cnt,
    round(buying_user_cnt/(select count(user_id) from user),1) as PUCHASED_RATIO
FROM tb
ORDER BY YEAR, MONTH