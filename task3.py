'''
Найдите общую сумму сделок по покупке одних компаний другими в долларах.
Отберите сделки, которые осуществлялись только за наличные с 2011 по 2013 год включительно.
'''

q3 = '''
SELECT SUM(price_amount)
FROM acquisition
WHERE CAST(acquired_at AS DATE) BETWEEN '2011-01-01' AND '2013-12-31'
      AND term_code = 'cash';
'''