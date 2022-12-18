'''
Составьте таблицу из полей:
name_of_fund — название фонда;
name_of_company — название компании;
amount — сумма инвестиций, которую привлекла компания в раунде.
В таблицу войдут данные о компаниях, в истории которых было
больше шести важных этапов, а раунды финансирования проходили
с 2012 по 2013 год включительно.
'''

q19 = '''
WITH
fund AS (SELECT id,
                name
         FROM fund),
comp AS (SELECT id,
                name,
                milestones
         FROM company),
roud AS (SELECT id,
                raised_amount,
                funded_at
         FROM funding_round),
inve As (SELECT id,
                funding_round_id,
                company_id,
                fund_id
         FROM investment)

SELECT fund.name AS name_of_fund,
       comp.name AS name_of_company,
       roud.raised_amount AS amount
FROM inve
LEFT OUTER JOIN fund ON inve.fund_id=fund.id
LEFT OUTER JOIN comp ON inve.company_id=comp.id
LEFT OUTER JOIN roud ON inve.funding_round_id=roud.id
WHERE comp.milestones > 6 AND
      EXTRACT(YEAR FROM CAST(roud.funded_at As DATE)) IN (2012, 2013) ;
'''