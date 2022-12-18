'''
Отберите данные по месяцам с 2010 по 2013 год, когда проходили
инвестиционные раунды. Сгруппируйте данные по номеру месяца
и получите таблицу, в которой будут поля:
номер месяца, в котором проходили раунды;
количество уникальных названий фондов из США, которые инвестировали в этом месяце;
количество компаний, купленных за этот месяц;
общая сумма сделок по покупкам в этом месяце.
'''

q22 = '''
WITH fundings AS (SELECT EXTRACT(MONTH FROM CAST(fr.funded_at AS DATE)) AS funding_month,
                         COUNT(DISTINCT f.id) AS us_funds
                  FROM fund AS f
                  LEFT JOIN investment AS i ON f.id = i.fund_id
                  LEFT JOIN funding_round AS fr ON i.funding_round_id = fr.id
                  WHERE f.country_code = 'USA'
                  AND EXTRACT(YEAR FROM CAST(fr.funded_at AS DATE)) BETWEEN 2010 AND 2013
                  GROUP BY funding_month),
acquisitions AS (SELECT EXTRACT(MONTH FROM CAST(acquired_at AS DATE)) AS funding_month,
                        COUNT(acquired_company_id) AS bought_co,
                        SUM(price_amount) AS sum_total
                 FROM acquisition
                 WHERE EXTRACT(YEAR FROM CAST(acquired_at AS DATE)) BETWEEN 2010 AND 2013
                 GROUP BY funding_month)
SELECT fnd.funding_month, fnd.us_funds, acq.bought_co, acq.sum_total
FROM fundings AS fnd
LEFT JOIN acquisitions AS acq ON fnd.funding_month = acq.funding_month;
'''