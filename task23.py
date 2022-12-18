'''
Составьте сводную таблицу и выведите среднюю сумму инвестиций для стран, 
в которых есть стартапы, зарегистрированные в 2011, 2012 и 2013 годах.
Данные за каждый год должны быть в отдельном поле. Отсортируйте таблицу
по среднему значению инвестиций за 2011 год от большего к меньшему.
'''

q23 = '''
WITH 
y_11 AS (SELECT country_code AS country,
         AVG(funding_total) AS y_2011
         FROM company
         WHERE EXTRACT(YEAR FROM founded_at::DATE) IN(2011, 2012, 2013)
         GROUP BY country, EXTRACT(YEAR FROM founded_at)
         HAVING EXTRACT(YEAR FROM founded_at) = '2011'),
y_12 AS (SELECT country_code AS country,
         AVG(funding_total) AS y_2012
         FROM company
         WHERE EXTRACT(YEAR FROM founded_at::DATE) IN(2011, 2012, 2013)
         GROUP BY country, EXTRACT(YEAR FROM founded_at)
         HAVING EXTRACT(YEAR FROM founded_at) = '2012'),
y_13 AS (SELECT country_code AS country,
         AVG(funding_total) AS y_2013
         FROM company
         WHERE EXTRACT(YEAR FROM founded_at::DATE) IN(2011, 2012, 2013)
         GROUP BY country, EXTRACT(YEAR FROM founded_at)
         HAVING EXTRACT(YEAR FROM founded_at) = '2013')
            SELECT y_11.country, y_2011, y_2012, y_2013
FROM y_11
JOIN y_12 ON y_11.country = y_12.country
JOIN y_13 ON y_12.country = y_13.country
ORDER BY y_2011 DESC;
'''