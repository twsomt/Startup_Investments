'''
Выгрузите таблицу, в которой будут такие поля:
название компании-покупателя;
сумма сделки;
название компании, которую купили;
сумма инвестиций, вложенных в купленную компанию;
доля, которая отображает, во сколько раз сумма покупки превысила сумму вложенных
в компанию инвестиций, округлённая до ближайшего целого числа.
Не учитывайте те сделки, в которых сумма покупки равна нулю. Если сумма инвестиций
в компанию равна нулю, исключите такую компанию из таблицы.
'''

q20 = '''
WITH
acqu AS (SELECT acquiring_company_id,
                acquired_company_id,
                price_amount
         FROM acquisition),
comp1 AS (SELECT id,
                name
         FROM company),
comp2 AS (SELECT id,
                name,
                funding_total
         FROM company)

SELECT comp1.name,
       acqu.price_amount,
       comp2.name,
       comp2.funding_total,
       ROUND(acqu.price_amount / comp2.funding_total, 0)
       
FROM acqu
LEFT OUTER JOIN comp1 ON acqu.acquiring_company_id=comp1.id
LEFT OUTER JOIN comp2 ON acqu.acquired_company_id=comp2.id
WHERE price_amount != 0 AND
      funding_total != 0
ORDER BY acqu.price_amount DESC,
         comp2.name
LIMIT 10 ;
'''