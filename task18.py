'''
Напишите похожий запрос: выведите среднее число учебных заведений 
(всех, не только уникальных), которые окончили сотрудники Facebook*.
*(сервис, запрещённый на территории РФ)
'''

q18 = '''
SELECT AVG(res.i)
FROM (SELECT ppls.id,
       COUNT(inst.instituition) AS i
FROM (
SELECT id
FROM people
WHERE company_id in (SELECT DISTINCT c.id
                     FROM company AS c
                     LEFT OUTER JOIN funding_round AS f ON c.id=f.company_id
                     WHERE name='Facebook')) AS ppls
LEFT OUTER JOIN education AS inst ON ppls.id=inst.person_id
WHERE inst.instituition IS NOT NULL
GROUP BY ppls.id ) AS res ;
'''