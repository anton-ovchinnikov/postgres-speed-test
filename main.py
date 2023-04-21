import datetime
import psycopg2

CICLES = 10

HOST = 'localhost'
DATABASE = 'speed_test'
USER = 'postgres'
PASSWORD = 'root'


def main():
    fresult = 0
    for n in range(1, CICLES + 1):
        print(f'>>>>>>>>>>---------- {n} ----------<<<<<<<<<<')

        name = 'Karl Basic'
        phone = '(08) 7766 5544'
        email = 'karlbasic@gmail.com'
        date = '2000-05-28 14:35:09'

        now = datetime.datetime.now().timestamp()
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        cursor = connection.cursor()

        cursor.execute('''INSERT INTO users(name, phone, email, date) VALUES(%s, %s, %s, %s);''',
                       (name, phone, email, date,))
        connection.commit()
        email_2 = 'karlbasic@gmail.com'
        cursor.execute('''UPDATE users SET email = %s WHERE name = %s''',
                       (email_2, name,))
        connection.commit()
        cursor.execute('''SELECT name FROM users WHERE name = %s''',
                       (name,))
        cursor.execute('''DELETE FROM users WHERE name = %s''',
                       (name,))
        connection.commit()

        connection.close()

        result = datetime.datetime.now().timestamp() - now
        fresult += result
        print(f'Результат: {result} сек.')

    fresult = fresult / CICLES
    print(f'Средний результат: {fresult} сек.')


if __name__ == '__main__':
    main()
