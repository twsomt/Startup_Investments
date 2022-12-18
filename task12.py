'''
Для каждой компании найдите количество учебных заведений,
которые окончили её сотрудники. Выведите название компании и число
уникальных названий учебных заведений. Составьте топ-5 компаний
по количеству университетов.
'''

q12 = '''
WITH
comp AS (SELECT id,
                name
         FROM company),

ppls AS (SELECT id,
                company_id
         FROM people),

inst AS (SELECT person_id,
                instituition
        from education)
        
SELECT comp.name,
       COUNT(DISTINCT inst.instituition)
FROM comp
LEFT OUTER JOIN ppls ON comp.id=ppls.company_id
LEFT OUTER JOIN inst ON ppls.id=inst.person_id
WHERE inst.instituition IS NOT NULL
GROUP BY comp.name
ORDER BY COUNT(inst.instituition) DESC
LIMIT 5 ;
'''