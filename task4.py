'''
Отобразите имя, фамилию и названия аккаунтов людей в твиттере,
у которых названия аккаунтов начинаются на 'Silver'.
'''

q4 = '''
SELECT first_name,
       last_name,
       twitter_username
FROM people
WHERE twitter_username LIKE 'Silver%' ;
'''