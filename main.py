import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )

    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT version();
        ''')
        print(f'Server version: {cursor.fetchone()}')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQl', _ex)
finally:
    # connection.close()
    cursor.close()
    print('[INFO] PostgreSQl connection closed')