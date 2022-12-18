'''
Составьте таблицу, куда войдут уникальные пары с номерами сотрудников
из предыдущей задачи и учебным заведением, которое окончил сотрудник.
'''

q15 = '''
SELECT DISTINCT ppls.id,
       inst.instituition
FROM (SELECT id
      FROM people
      WHERE company_id in (SELECT DISTINCT c.id
                        FROM company AS c
                        LEFT OUTER JOIN funding_round AS f ON c.id=f.company_id
                        WHERE status = 'closed' AND
                              is_first_round  = 1 AND
                              is_last_round = 1)) AS ppls
      LEFT OUTER JOIN education AS inst ON ppls.id=inst.person_id
WHERE inst.instituition IS NOT NULL ;
'''