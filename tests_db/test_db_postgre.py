
import psycopg2
import time

import pytest

class TestsDBPostgre:

    @pytest.mark.skip
    def test_sample_query(self):

        # Устанавливаем соединение с БД
        connection = psycopg2.connect(dbname="dbname", user="user", password="password", host="host", port="port")
        print("\n")
        print("Установлено соединение с БД.")

        # Создаем курсор
        cursor = connection.cursor()

        # Делаем select в БД
        sql_query = "select * from table limit 10"
        cursor.execute(sql_query)
        connection.commit()
        #time.sleep(1)

        # Результат
        results = cursor.fetchall()

        # Выводим результат
        for result in results: print(result)

        cursor.close()
        connection.close()
        print("\n")
        print("Соединение с БД закрыто.")

