from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import server
import sys
from interface1 import Ui_MainWindow
from Error_class import ErrorDialog
import pymysql

def change_page(window, num):
    window.stackedWidget.setCurrentIndex(num)

def auth_user(window, app):
    global connection
    global starter_page
    try:
        connection = pymysql.connect(
        host= server.host_server,
        user= window.login_line.text(),
        password= window.password_line.text(),
        database="main_chena"
        )
        global cursor
        cursor = connection.cursor()
        cursor.execute("SELECT admin FROM users WHERE Login = %s", (window.login_line.text(),))
        results = cursor.fetchall()
        if len(results) == 1:
            admin = results[0][0]
            if admin == 1:
                change_page(window, 2)
                starter_page = 2
            if admin == 0:
                change_page(window, 1)
                starter_page = 1
            initiliaze_button(window)
            app.showMaximized() 
    except pymysql.MySQLError as err:
        window.label_21.setText(f"Ошибка: {err}")
        window.label_21.setStyleSheet("color: red")


def Add_emp(window):
    Surname = window.Surname.text()
    Firstname = window.Firstname.text()
    Patronymic = window.Patronymic.text()
    Adress = window.Adress.text()
    Number = window.Number.text()
    Station = window.Station.text()
    try:
        Admin = window.Admin.text()
        Admin = int(Admin)
    except:
        Error = ErrorDialog("Поле админ должно быть числом")
        window.Admin.setText("")
        return 0
    Login = window.Login_line_emp.text()
    Password = window.Password_line_emp.text()
    cursor.execute(f"INSERT INTO users (Surname, Firstname, Patronymic, Adress, Num, Admin, Login) VALUES (%s, %s, %s, %s, %s, %s, %s);", (Surname, Firstname, Patronymic, Adress, Number, int(Admin), Login))
    cursor.execute(f"CREATE USER '{Login}'@'%' IDENTIFIED BY '{Password}';")
    if Admin == 0:
        cursor.execute(f"GRANT SELECT, INSERT ON main_chena.* TO '{Login}'@'%';")
    if Admin == 1:
        cursor.execute(f"GRANT ALL PRIVILEGES ON *.* TO '{Login}'@'%';")
    cursor.execute("FLUSH PRIVILEGES;")
    connection.commit()
    Fill_table_emp(window)

def Edit_emp(window):
    Surname = window.Surname.text()
    Firstname = window.Firstname.text()
    Patronymic = window.Patronymic.text()
    Adress = window.Adress.text()
    Number = window.Number.text()
    Station = window.Station.text()
    try:
        Admin = window.Admin.text()
        Admin = int(Admin)
    except:
        Error = ErrorDialog("Поле админ должно быть числом")
        window.Admin.setText("")
        return 0
    Login = window.Login_line_emp.text()
    Password = window.Password_line_emp.text()
    cursor.execute(f"UPDATE users SET Surname = %s, Firstname = %s, Patronymic = %s, Adress = %s, Num = %s, Admin = %s WHERE Login = %s;", (Surname, Firstname, Patronymic, Adress, Number, int(Admin), Login))
    if Admin == 0:
        cursor.execute(f"REVOKE ALL PRIVILEGES, GRANT OPTION FROM '{Login}'@'%';")
        cursor.execute(f"GRANT SELECT, INSERT ON main_chena.* TO '{Login}'@'%';")
    if Admin == 1:
        cursor.execute(f"GRANT ALL PRIVILEGES ON *.* TO '{Login}'@'%';")
    cursor.execute("FLUSH PRIVILEGES;")
    connection.commit()
    Fill_table_emp(window)

def Fill_lineedit_emp(window, red):
    if red == 0:
        window.Surname.setText("")
        window.Firstname.setText("")
        window.Patronymic.setText("")
        window.Adress.setText("")
        window.Number.setText("")
        window.Station.setText("")
        window.Admin.setText("")
        window.Login_line_emp.setText("")
        window.Password_line_emp.setText("")
        window.Save_emp_add.clicked.disconnect()
        window.Save_emp_add.clicked.connect(lambda: Add_emp(window))
    else:
        currect = window.Table_emp.currentRow()
        window.Surname.setText(f"{window.Table_emp.item(currect, 1).text()}")
        window.Firstname.setText(f"{window.Table_emp.item(currect, 2).text()}")
        window.Patronymic.setText(f"{window.Table_emp.item(currect, 3).text()}")
        window.Adress.setText(f"{window.Table_emp.item(currect, 4).text()}")
        window.Number.setText(f"{window.Table_emp.item(currect, 5).text()}")
        window.Station.setText(f"")
        window.Admin.setText(f"{window.Table_emp.item(currect, 6).text()}")
        window.Login_line_emp.setText(f"{window.Table_emp.item(currect, 7).text()}")
        window.Password_line_emp.setText(f"")
        window.Save_emp_add.clicked.disconnect()
        window.Save_emp_add.clicked.connect(lambda: Edit_emp(window))
    change_page(window, 6)

def Remove_emp(window):
    currect = window.Table_emp.currentRow()
    login = window.Table_emp.item(currect, 7).text()
    cursor.execute("DELETE FROM users WHERE login = %s", (login,))
    cursor.execute(f"DROP USER '{login}'@'%';")
    Fill_table_emp(window)

def Fill_table_emp(window):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    if (len(rows) == 0):
        change_page(window, 3)
        return 0
    window.Table_emp.setColumnCount(len(rows[0]))
    window.Table_emp.setRowCount(len(rows))
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            font = QFont()
            font.setPointSize(14)
            Item = QTableWidgetItem(str(rows[i][j]))
            Item.setFlags(Item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            Item.setFont(font)
            window.Table_emp.setItem(i, j, Item)
    change_page(window, 3)



def setup_login(window, app):
    app.resize(230,350)
    window.Login_b.clicked.connect(lambda :  auth_user(window, app))


def Fill_table_station(window):
    cursor.execute("SELECT idstation, Name,  ST_asText(Coordinate) FROM station")
    rows = cursor.fetchall()
    if (len(rows) == 0):
        change_page(window, 4)
        return 0
    window.Table_station.setColumnCount(len(rows[0]))
    window.Table_station.setRowCount(len(rows))
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            font = QFont()
            font.setPointSize(14)
            Item = QTableWidgetItem(str(rows[i][j]))
            Item.setFlags(Item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            Item.setFont(font)
            window.Table_station.setItem(i, j, Item)
    change_page(window, 4)

def check_coordinates(latitude, longitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        return True
    return False

def Fill_lineedit_station(window, red):
    if red == 0:
        window.Name_station.setText("")
        window.Coordinate.setText("")
        window.Save_station_add.clicked.disconnect()
        window.Save_station_add.clicked.connect(lambda: Add_station(window))
    else:
        currect = window.Table_station.currentRow()
        window.Name_station.setText(f"{window.Table_station.item(currect, 1).text()}")
        Coordinate = window.Table_station.item(currect, 2).text()
        Coordinate = Coordinate.replace('POINT(', '')
        Coordinate = Coordinate.replace(')', '')
        window.Coordinate.setText(f"{Coordinate}")
        window.Save_station_add.clicked.disconnect()
        window.Save_station_add.clicked.connect(lambda: Edit_station(window, currect))
    change_page(window, 7)

def Add_station(window):
    Name = window.Name_station.text()
    Coordinate = window.Coordinate.text()
    Coordinate = Coordinate.split(" ")
    if (len(Coordinate) == 1):
        Error = ErrorDialog("Проверьте корректность координат(Пример: -45 -100)")
        window.Admin.setText("")
        return 0
    try:
        latitude = int(Coordinate[0])
        longitude = int(Coordinate[1])
    except:
        Error = ErrorDialog("Долгота и широта должны быть числами(Пример: -45 -100)")
        window.Admin.setText("")
        return 0
    if (not check_coordinates(latitude, longitude)):
        Error = ErrorDialog("Проверьте корректность координат(Пример: -45 -100)")
        window.Admin.setText("")
        return 0
    cursor.execute(f"INSERT INTO station (Name, Coordinate) VALUES (%s, Point(%s, %s));", (Name, latitude, longitude))
    connection.commit()
    Fill_table_station(window)

def Edit_station(window, currect_row):
    Name = window.Name_station.text()
    Coordinate = window.Coordinate.text()
    Coordinate = Coordinate.split(" ")
    if (len(Coordinate) == 1):
        Error = ErrorDialog("Проверьте корректность координат(Пример: -45 -100)")
        window.Admin.setText("")
        return 0
    try:
        latitude = int(Coordinate[0])
        longitude = int(Coordinate[1])
    except:
        Error = ErrorDialog("Долгота и широта должны быть числами(Пример: -45 -100)")
        window.Admin.setText("")
        return 0
    if (not check_coordinates(latitude, longitude)):
        Error = ErrorDialog("Проверьте корректность координат(Пример: -45 -100)")
        window.Admin.setText("")
        return
    id =  window.Table_station.item(currect_row, 0).text()
    cursor.execute(f"UPDATE station SET Name = %s, Coordinate = Point(%s, %s)  WHERE idstation = %s;", (Name, latitude, longitude, id))
    connection.commit()
    Fill_table_station(window)

def Remove_station(window):
    currect = window.Table_station.currentRow()
    id = window.Table_station.item(currect, 0).text()
    cursor.execute("DELETE FROM station WHERE idstation = %s", (id,))
    Fill_table_station(window)

def initiliaze_button(window):
    #Окно входа

    #Окно метеоролога
    #Кнопка добавить замер
    window.Add_izm.clicked.connect(lambda: change_page(window, 8))
    #Кнопка просмотр статистики
    window.Statitic_view_user.clicked.connect(lambda: change_page(window, 9))

    #Окно администратора
    #Окно управления метеорологами
    window.Emp_view.clicked.connect(lambda :  Fill_table_emp(window))
    #Окно управления станциями
    window.Station_view.clicked.connect(lambda: Fill_table_station(window))
    #Окно управления измерениями
    window.Izm_view.clicked.connect(lambda: change_page(window, 5))
    #Окно статистики 
    window.Statistic_view_admin.clicked.connect(lambda: change_page(window, 9))

    #Окно управления пользователями
    window.Add_emp.clicked.connect(lambda: Fill_lineedit_emp(window, 0))
    window.Redac_emp.clicked.connect(lambda: Fill_lineedit_emp(window, 1))
    window.Back_emp.clicked.connect(lambda: change_page(window, starter_page))
    window.Del_emp.clicked.connect(lambda: Remove_emp(window))

    #Окно управления станциями
    window.Add_station.clicked.connect(lambda: Fill_lineedit_station(window, 0))
    window.Red_station.clicked.connect(lambda: Fill_lineedit_station(window, 1))
    window.Back_station.clicked.connect(lambda: change_page(window, starter_page))
    window.Del_station.clicked.connect(lambda: Remove_station(window))

    #Окно управления измерениями
    window.Add_izm_2.clicked.connect(lambda: change_page(window, 8))
    window.Red_izm.clicked.connect(lambda: change_page(window, 8))
    window.Back_izm.clicked.connect(lambda: change_page(window, starter_page))
    #window.Del_izm.clicked.connect()

    #Окно добавления метеорологов
    window.Back_emp_add.clicked.connect(lambda: Fill_table_emp(window))
    window.Save_emp_add.clicked.connect(lambda: Add_emp(window))

    #Окно добавления станций
    window.Back_station_add.clicked.connect(lambda: change_page(window, 4))
    window.Save_station_add.clicked.connect(lambda: Add_station(window))

    #Окно добавления измерений
    if starter_page == 1:
        window.Back_izm_add.clicked.connect(lambda: change_page(window, starter_page))
    else :
        window.Back_izm_add.clicked.connect(lambda: change_page(window, 5))
    #window.Save_izm_add.clicked.connect()

    #Окно статистики
    if starter_page == 1:
        window.Back_stat.clicked.connect(lambda: change_page(window, starter_page))
    else :
        window.Back_stat.clicked.connect(lambda: change_page(window, 2))
    
    #window.Create_stat.clicked.connect(lambda: change_page(window, 4))
    #window.Save_word_stat.clicked.connect(lambda: change_page(window, 4))

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setMinimumSize(230,350)
    
    Content_main_window = Ui_MainWindow()
    Content_main_window.setupUi(main_window)
    global starter_page
    starter_page = 0
    global cursor
    cursor = 0
    setup_login(Content_main_window, main_window)
    main_window.show()
    
    sys.exit(app.exec())
