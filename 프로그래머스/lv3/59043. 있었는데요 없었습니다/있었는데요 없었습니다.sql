-- 코드를 입력하세요
SELECT
ins.animal_id as ANIMAL_ID,
ins.name as NAME

FROM ANIMAL_INS as ins  
INNER JOIN ANIMAL_OUTS as outs 
on ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE
    ins.DATETIME > outs.DATETIME
ORDER BY ins.DATETIME