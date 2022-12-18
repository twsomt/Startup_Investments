'''
Выгрузите таблицу, в которую войдут названия компаний из категории social,
получившие финансирование с 2010 по 2013 год включительно. Проверьте,
что сумма инвестиций не равна нулю. Выведите также номер месяца,
в котором проходил раунд финансирования.
'''

q21 = '''
WITH
comp AS (SELECT id,
                name,
                category_code
         FROM company),
foud AS (SELECT company_id,
                funded_at,
                raised_amount
         FROM funding_round)
         
SELECT comp.name,
       EXTRACT(MONTH FROM CAST(foud.funded_at AS DATE))
FROM comp
LEFT OUTER JOIN foud ON comp.id=foud.company_id
WHERE comp.category_code = 'social' AND
      foud.raised_amount != 0 AND
      CAST(foud.funded_at AS DATE) BETWEEN '2010-01-01' AND '2013-12-31' ;
'''