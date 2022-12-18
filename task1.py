'''
Посчитайте, сколько компаний закрылось.
'''

q1 = '''
SELECT COUNT(status)
FROM company
WHERE status = 'closed';
'''