import mysql.connector

# Подключение к базе данных
connection = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Admin123",
    database="main_chena"
)

cursor = connection.cursor()
login = "Admin"
# Выполнение запроса
cursor.execute(f"SELECT surname, password FROM users WHERE surname = \"{login}\"")


# Получение данных
results = cursor.fetchall()
for row in results:
    print(row)

# Закрытие соединения
cursor.close()
connection.close()
