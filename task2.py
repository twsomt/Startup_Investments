'''
Отобразите количество привлечённых средств для новостных компании США.
Используйте данные из таблицы company. Отсортируйте таблицу по убыванию значений в поле funding_total.
'''

q2 = '''
SELECT funding_total
FROM company
WHERE country_code = 'USA'
      AND category_code = 'news'
ORDER BY funding_total DESC ;
'''