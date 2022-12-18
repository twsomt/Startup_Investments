'''
Выведите на экран всю информацию о людях, у которых названия аккаунтов
в твиттере содержат подстроку 'money', а фамилия начинается на 'K'.
'''

q5 = '''
SELECT *
FROM people
WHERE twitter_username LIKE '%money%'
      AND last_name LIKE 'K%';
'''