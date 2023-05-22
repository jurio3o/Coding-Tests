WITH tb AS (
    SELECT mp.MEMBER_ID, MEMBER_NAME
    FROM MEMBER_PROFILE as mp
    JOIN (
        SELECT 
            MEMBER_ID, 
            count(*) as review_cnt 
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY review_cnt DESC
        limit 1
    ) as rr
    ON mp.MEMBER_ID = rr.MEMBER_ID
)
SELECT 
    MEMBER_NAME, 
    REVIEW_TEXT, 
    DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM tb
JOIN REST_REVIEW 
on tb.MEMBER_ID = REST_REVIEW.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT