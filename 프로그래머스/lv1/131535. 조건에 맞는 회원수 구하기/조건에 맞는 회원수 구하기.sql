-- 코드를 입력하세요
SELECT count(user_id) FROM USER_INFO
WHERE EXTRACT(YEAR FROM JOINED) = 2021
AND AGE BETWEEN 20 AND 29