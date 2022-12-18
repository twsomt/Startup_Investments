'''
Для каждой из категорий, назначенных в предыдущем задании, посчитайте округлённое
до ближайшего целого числа среднее количество инвестиционных раундов, в которых
фонд принимал участие. Выведите на экран категории и среднее число инвестиционных
раундов. Отсортируйте таблицу по возрастанию среднего.
'''

q9 = '''
SELECT CASE
           WHEN invested_companies>=100 THEN 'high_activity'
           WHEN invested_companies>=20 THEN 'middle_activity'
           ELSE 'low_activity'
       END AS activity,
       ROUND(AVG(investment_rounds), 0) AS avg_activity
FROM fund
GROUP BY activity
ORDER BY avg_activity ASC ;
'''