'''
Составьте список уникальных номеров сотрудников,
которые работают в компаниях, отобранных в предыдущем задании.
'''

q14 = '''
SELECT id
FROM people
WHERE company_id in (SELECT DISTINCT c.id
                     FROM company AS c
                     LEFT OUTER JOIN funding_round AS f ON c.id=f.company_id
                     WHERE status = 'closed' AND
                           is_first_round  = 1 AND
                           is_last_round = 1) ;
'''