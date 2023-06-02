"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


def get_data_table(path):
    """Возвращает данные, полученные из файла"""
    new_list = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for line in reader:
            new_list.append(line)
    return new_list[1:len(new_list) + 1]


def main():
    """Функция записывает информацию из файлов БД"""
    # подключение к БД
    con = psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password='14745852'
    )
           # добавление coursor
    with con.cursor() as cur:
        #Заполнение таблицы customers
            data = get_data_table('north_data/customers_data.csv')
            for i in range(0, len(data)):
               cur.execute('INSERT INTO customers VALUES (%s,%s,%s)',
                           (data[i][0], data[i][1], data[i][2]))
        # Заполнение таблицы employees
            data = get_data_table('north_data/employees_data.csv')
            for i in range(0, len(data)):
               cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s)',
                           ((i+1), data[i][0], data[i][1], data[i][2],
                            data[i][3], data[i][4]))
        # Заполнение таблицы orders
            data = get_data_table('north_data/orders_data.csv')
            for i in range(0, len(data)):
                cur.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s)',
                            (data[i][0], data[i][1], data[i][2],
                             data[i][3], data[i][4]))

            cur.execute('SELECT*FROM orders')
            rows = cur.fetchall()
            for row in rows:
                # for row in data:
                print(row)
    con.commit()
    con.close()


if __name__ == '__main__':
    main()
