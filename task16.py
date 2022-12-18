'''
Посчитайте количество учебных заведений для каждого сотрудника из предыдущего задания.
При подсчёте учитывайте, что некоторые сотрудники могли окончить одно и то же заведение дважды.
'''

q16 = '''
SELECT ppls.id,
       COUNT(inst.instituition)
FROM (
SELECT id
FROM people
WHERE company_id in (SELECT DISTINCT c.id
                     FROM company AS c
                     LEFT OUTER JOIN funding_round AS f ON c.id=f.company_id
                     WHERE status = 'closed' AND
                           is_first_round  = 1 AND
                           is_last_round = 1)) AS ppls
LEFT OUTER JOIN education AS inst ON ppls.id=inst.person_id
WHERE inst.instituition IS NOT NULL
GROUP BY ppls.id ;
'''