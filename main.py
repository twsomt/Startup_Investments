import psycopg2
from config import host, user, password, db_name
from task1 import q1
from task2 import q2
from task3 import q3
from task4 import q4
from task5 import q5
from task6 import q6
from task7 import q7
from task8 import q8
from task9 import q9
from task10 import q10
from task11 import q11
from task12 import q12
from task13 import q13
from task14 import q14
from task15 import q15
from task16 import q16
from task17 import q17
from task18 import q18
from task19 import q19
from task20 import q20
from task21 import q21
from task22 import q22
from task23 import q23

tasks = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
         q11, q12, q13, q14, q15, q16, q17, q18, q19, q20,
         q21, q22, q23)

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )

    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        for task in tasks:
            cursor.execute(f'''
            {task}
            ''')
        print()
        #print(f'Server version: {cursor.fetchone()}')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQl', _ex)
finally:
    # connection.close()
    cursor.close()
    print('[INFO] PostgreSQl connection closed')