'''
Составьте список с уникальными названиями закрытых компаний,
для которых первый раунд финансирования оказался последним.
'''

q13 = '''
SELECT DISTINCT c.name
FROM company AS c
LEFT OUTER JOIN funding_round AS f ON c.id=f.company_id
WHERE status = 'closed' AND
      is_first_round  = 1 AND
      is_last_round = 1 ;
'''