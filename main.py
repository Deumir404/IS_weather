from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import server
import sys
from interface1 import Ui_MainWindow
from Error_class import ErrorDialog
import pymysql
from datetime import datetime, date
from docx import Document 

def change_page(window, num):
    window.stackedWidget.setCurrentIndex(num)

def setup_login(window, app):
    app.resize(230,350)
    window.Login_b.clicked.connect(lambda :  auth_user(window, app))

def auth_user(window, app):
    global connection
    global starter_page
    try:
        connection = pymysql.connect(
        host= server.host_server,
        user= window.login_line.text(),
        password= window.password_line.text(),
        database="weather"
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
    Station = window.Station.currentText()
    Station = int(Station.split(" ")[0])
    try:
        Admin = window.Admin.text()
        Admin = int(Admin)
        if Admin != 0 and Admin != 1:
            raise
    except:
        Error = ErrorDialog("Поле админ должно быть числом от 0 до 1")
        window.Admin.setText("")
        return 0
    Login = window.Login_line_emp.text()
    Password = window.Password_line_emp.text()
    cursor.execute(f"INSERT INTO users (Surname, Firstname, Patronymic, Adress, Num, Admin, Login, Station) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (Surname, Firstname, Patronymic, Adress, Number, int(Admin), Login, Station))
    cursor.execute(f"CREATE USER '{Login}'@'%' IDENTIFIED BY '{Password}';")
    if Admin == 0:
        cursor.execute(f"GRANT SELECT, INSERT ON weather.* TO '{Login}'@'%';")
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
    Station = window.Station.currentText()
    Station = int(Station.split(" ")[0])
    try:
        Admin = window.Admin.text()
        Admin = int(Admin)
    except:
        Error = ErrorDialog("Поле админ должно быть числом")
        window.Admin.setText("")
        return 0
    Login = window.Login_line_emp.text()
    Password = window.Password_line_emp.text()
    cursor.execute(f"UPDATE users SET Surname = %s, Firstname = %s, Patronymic = %s, Adress = %s, Num = %s, Admin = %s, Station = %s WHERE Login = %s;", (Surname, Firstname, Patronymic, Adress, Number, int(Admin), Station, Login))
    if Admin == 0:
        cursor.execute(f"REVOKE ALL PRIVILEGES, GRANT OPTION FROM '{Login}'@'%';")
        cursor.execute(f"GRANT SELECT, INSERT ON weather.* TO '{Login}'@'%';")
    if Admin == 1:
        cursor.execute(f"GRANT ALL PRIVILEGES ON *.* TO '{Login}'@'%';")
    cursor.execute("FLUSH PRIVILEGES;")
    connection.commit()
    Fill_table_emp(window)

def Fill_lineedit_emp(window, red):
    window.Station.clear()
    cursor.execute("SELECT `idstation`, `name` FROM station")
    station_in_db = cursor.fetchall()
    station_ids = [str(station[0]) + " " + str(station[1]) for station in station_in_db]
    window.Station.addItems(station_ids)
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
        try:
            window.Save_emp_add.clicked.disconnect()
        except: 
            pass
        window.Save_emp_add.clicked.connect(lambda: Add_emp(window))
    else:
        try:
            currect = window.Table_emp.currentRow()
            if currect == -1:
                raise
        except:
            error = ErrorDialog("Выберите строку для редактирования")
            error.show()
            return 0
        window.Surname.setText(f"{window.Table_emp.item(currect, 1).text()}")
        window.Firstname.setText(f"{window.Table_emp.item(currect, 2).text()}")
        window.Patronymic.setText(f"{window.Table_emp.item(currect, 3).text()}")
        window.Adress.setText(f"{window.Table_emp.item(currect, 4).text()}")
        window.Number.setText(f"{window.Table_emp.item(currect, 5).text()}")
        window.Station.setCurrentIndex(0)
        window.Admin.setText(f"{window.Table_emp.item(currect, 6).text()}")
        window.Login_line_emp.setText(f"{window.Table_emp.item(currect, 7).text()}")
        window.Password_line_emp.setText(f"")
        try:
            window.Save_emp_add.clicked.disconnect()
        except: 
            pass
        window.Save_emp_add.clicked.connect(lambda: Edit_emp(window))
    change_page(window, 6)

def Remove_emp(window):
    currect = window.Table_emp.currentRow()
    login = window.Table_emp.item(currect, 7).text()
    try:
        cursor.execute("DELETE FROM users WHERE login = %s", (login,))
        cursor.execute(f"DROP USER '{login}'@'%';")
    except pymysql.MySQLError as err:
        error = ErrorDialog(str(err))
        error.show()
    Fill_table_emp(window)

def Fill_table_emp(window):
    cursor.execute("SELECT `idUsers`,`Surname`,`Firstname`,`Patronymic`,`Adress`,`Num`,`Admin`,`Login`, `Station` FROM users")
    rows = cursor.fetchall()
    if (len(rows) == 0):
        change_page(window, 3)
        return 0
    window.Table_emp.setColumnCount(len(rows[0]))
    window.Table_emp.setRowCount(len(rows))
    window.Table_emp.setHorizontalHeaderLabels(['ID', 'Фамилия', 'Имя', 'Отчество', 'Адрес', 'Номер телефона', 'Админ?', 'Логин', 'Станция'])
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            font = QFont()
            font.setPointSize(14)
            Item = QTableWidgetItem(str(rows[i][j]))
            Item.setFlags(Item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            Item.setFont(font)
            window.Table_emp.setItem(i, j, Item)
    window.Table_emp.resizeColumnsToContents()
    window.Table_emp.resizeRowsToContents()   
    change_page(window, 3)


def Fill_table_station(window):
    cursor.execute("SELECT idstation, Name,  ST_asText(Coordinate) FROM station")
    rows = cursor.fetchall()
    if (len(rows) == 0):
        change_page(window, 4)
        return 0
    window.Table_station.setColumnCount(len(rows[0]))
    window.Table_station.setRowCount(len(rows))
    window.Table_station.setHorizontalHeaderLabels(['ID', 'Название', 'Координаты'])
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            font = QFont()
            font.setPointSize(14)
            Item = QTableWidgetItem(str(rows[i][j]))
            Item.setFlags(Item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            Item.setFont(font)
            window.Table_station.setItem(i, j, Item)
    window.Table_station.resizeColumnsToContents()
    window.Table_station.resizeRowsToContents()        
    change_page(window, 4)

def check_coordinates(latitude, longitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        return True
    return False

def Fill_lineedit_station(window, red):
    if red == 0:
        window.Name_station.setText("")
        window.Coordinate.setText("")
        try:
            window.Save_station_add.clicked.disconnect()
        except:
            pass
        window.Save_station_add.clicked.connect(lambda: Add_station(window))
    else:
        try:
            currect = window.Table_station.currentRow()
            if currect == -1:
                raise
        except:
            error = ErrorDialog("Выберите строку для редактирования")
            error.show()
            return 0
        window.Name_station.setText(f"{window.Table_station.item(currect, 1).text()}")
        Coordinate = window.Table_station.item(currect, 2).text()
        Coordinate = Coordinate.replace('POINT(', '')
        Coordinate = Coordinate.replace(')', '')
        window.Coordinate.setText(f"{Coordinate}")
        try:
            window.Save_station_add.clicked.disconnect()
        except:
            pass
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
    try:
        cursor.execute("DELETE FROM station WHERE idstation = %s", (id,))
    except pymysql.MySQLError as err:
        error = ErrorDialog(str(err))
        error.show()
    Fill_table_station(window)



def Fill_lineedit_izm(window, red):
    if red == 0:
        window.Time.setText(f"{datetime.now()}")
        window.Time.setEnabled(False)
        window.Temp.setText("")
        window.humidity.setText("")
        window.precipitation.setText("")
        window.direction_wind.setText("")
        window.Wind_speed.setText("")
        try:
            window.Save_izm_add.clicked.disconnect()
        except: 
            pass
        window.Save_izm_add.clicked.connect(lambda: Add_measure(window))
    else:
        try:
            currect = window.Table_izm.currentRow()
            if currect == -1:
                raise
        except:
            error = ErrorDialog("Выберите строку для редактирования")
            error.show()
            return 0
        window.Time.setText(f"{window.Table_izm.item(currect, 3).text()}")
        window.Time.setEnabled(False)
        window.Temp.setText(f"{window.Table_izm.item(currect, 4).text()}")
        window.humidity.setText(f"{window.Table_izm.item(currect, 5).text()}")
        window.precipitation.setText(f"{window.Table_izm.item(currect, 6).text()}")
        window.direction_wind.setText(f"{window.Table_izm.item(currect, 7).text()}")
        window.Wind_speed.setText(f"{window.Table_izm.item(currect, 8).text()}")
        try:
            window.Save_izm_add.clicked.disconnect()
        except: 
            pass
        window.Save_izm_add.clicked.connect(lambda: Edit_measure(window, currect))
    change_page(window, 8)

def Add_measure(window):
    time = window.Time.text()
    temp = window.Temp.text()
    try:
        temp = float(temp)
    except:
        e = ErrorDialog("Ошибка температура должна быть числом")
        e.show()
        return 0
    humidity = window.humidity.text()
    try:
        humidity = float(humidity)
        if not 0 <= humidity <= 100:
            raise
    except:
        e = ErrorDialog("Ошибка влажность должна быть числом в процентах")
        e.show()
        return 0
    precipitation = window.precipitation.text()
    try:
        precipitation = float(precipitation)
    except:
        e = ErrorDialog("Ошибка осадки должны быть числом")
        e.show()
        return 0
    direction_wind = window.direction_wind.text()
    try:
        direction_wind = float(direction_wind)
        if  not 0 <= direction_wind <= 360:
            raise
    except:
        e = ErrorDialog("Ошибка направление ветра должно быть числом в градусах в пределах от 0 до 360")
        e.show()
        return 0
    wind_speed = window.Wind_speed.text()
    try:
        wind_speed = float(wind_speed)
    except:
        e = ErrorDialog("Ошибка скорость ветра должно быть числом")
        e.show()
        return 0
    user = cursor.execute("Select idUsers from users WHERE login = %s", (window.login_line.text(),))
    user = cursor.fetchone()[0]
    station = cursor.execute("Select Station from users WHERE login = %s", (window.login_line.text(),))
    station = cursor.fetchone()[0]
    cursor.execute(f"INSERT INTO measure (id_station, id_user, Time, Temp, Humadity, Precepit, `Wind speed`, `Wind direction`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (station, user, time, temp, humidity, precipitation, wind_speed, direction_wind))
    connection.commit()
    Fill_table_measure(window)
    


def Edit_measure(window, currect_row):
    time = window.Time.text()
    temp = window.Temp.text()
    try:
        temp = float(temp)
    except:
        e = ErrorDialog("Ошибка температура должна быть числом")
        e.show()
        return 0
    humidity = window.humidity.text()
    try:
        humidity = float(humidity)
        if not 0 <= humidity <= 100:
            raise
    except:
        e = ErrorDialog("Ошибка влажность должна быть числом в процентах")
        e.show()
        return 0
    precipitation = window.precipitation.text()
    try:
        precipitation = float(precipitation)
    except:
        e = ErrorDialog("Ошибка осадки должны быть числом")
        e.show()
        return 0
    direction_wind = window.direction_wind.text()
    try:
        direction_wind = float(direction_wind)
        if  not 0 <= direction_wind <= 360:
            raise
    except:
        e = ErrorDialog("Ошибка направление ветра должно быть числом в градусах в пределах от 0 до 360")
        e.show()
        return 0
    wind_speed = window.Wind_speed.text()
    try:
        wind_speed = float(wind_speed)
    except:
        e = ErrorDialog("Ошибка скорость ветра должно быть числом")
        e.show()
        return 0
    id = window.Table_izm.item(currect_row, 0).text()
    cursor.execute(f"UPDATE measure SET Temp = %s, Humadity = %s, Precepit = %s, `Wind speed` = %s, `Wind direction` = %s WHERE idmeasure = %s;", (temp, humidity, precipitation, direction_wind, wind_speed , id))
    connection.commit()
    Fill_table_measure(window)

def Fill_table_measure(window):
    try:
        window.Station_izm.currentIndexChanged.disconnect()
    except:
        pass
    index = window.Station_izm.currentIndex()
    window.Station_izm.clear()
    cursor.execute("SELECT `idstation`, `name` FROM station")
    station_in_db = cursor.fetchall()
    station_ids = [str(station[0]) + " " + str(station[1]) for station in station_in_db]
    station_ids.insert(0, "")
    window.Station_izm.addItems(station_ids)
    window.Station_izm.setCurrentIndex(index)
    window.Station_izm.currentIndexChanged.connect(lambda: Fill_table_measure(window))

    if window.Station_izm.currentText() == "":
        cursor.execute("SELECT `idmeasure`, `Name`, `Login`, `Time`, `Temp`, `Humadity`, `Precepit`, `Wind speed`, `Wind direction` FROM `measure` LEFT JOIN `users` ON `Id_user` = `idUsers` LEFT JOIN `station` ON `Id_station` = `idstation`;")
    else :
        
        id = window.Station_izm.currentText()
        id = int(id.split(" ")[0])
        cursor.execute("SELECT `idmeasure`, `Name`, `Login`, `Time`, `Temp`, `Humadity`, `Precepit`, `Wind speed`, `Wind direction` FROM `measure` LEFT JOIN `users` ON `Id_user` = `idUsers` LEFT JOIN `station` ON `Id_station` = `idstation` WHERE `idstation` = %s;", (id, ))
    rows = cursor.fetchall()
    if (len(rows) == 0):
        window.Table_izm.setColumnCount(0)
        window.Table_izm.setRowCount(0)
        change_page(window, 5)
        return 0
    window.Table_izm.setColumnCount(len(rows[0]))
    window.Table_izm.setRowCount(len(rows))
    window.Table_izm.setHorizontalHeaderLabels(['ID', 'Станция', 'Метеоролог', 'Время замера', 'Температура',  'Влажность',  'Осадки',  'Скорость ветра',  'Направление ветра'])
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            font = QFont()
            font.setPointSize(14)
            Item = QTableWidgetItem(str(rows[i][j]))
            Item.setFlags(Item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            Item.setFont(font)
            window.Table_izm.setItem(i, j, Item)
    window.Table_izm.resizeColumnsToContents()
    window.Table_izm.resizeRowsToContents()
    change_page(window, 5)

def Remove_measure(window):
    currect = window.Table_izm.currentRow()
    id = window.Table_izm.item(currect, 0).text()
    try:
        cursor.execute("DELETE FROM measure WHERE idmeasure = %s", (id,))
    except pymysql.MySQLError as err:
        error = ErrorDialog(str(err))
        error.show()
    Fill_table_measure(window)


def fill_combobox(window):
    window.Begin_period.setText("1970-1-1")
    window.End_period.setText(str(datetime.now().date()))
    cursor.execute("SELECT `idstation`, `name` FROM station")
    station_in_db = cursor.fetchall()
    station_ids = [str(station[0]) + " " + str(station[1]) for station in station_in_db]
    window.Station_stat.addItems(station_ids)
    change_page(window, 9)

def create_statistic(window):
    window.Table_stat.setColumnCount(5)
    window.Table_stat.setRowCount(5)
    window.Table_stat.setHorizontalHeaderLabels(['Минимум', 'Среднее', 'Максимальное', 'Дисперсия', 'Стандартное отклонение'])
    window.Table_stat.setVerticalHeaderLabels(['Температура', 'Влажность', 'Осадки', 'Скорость ветра', 'Направление ветра'])
    begin_period = window.Begin_period.text()
    if begin_period == "":
        begin_period = date(1970, 1, 1)
    end_period = window.End_period.text()
    if end_period == "":
        end_period = datetime.now().date()
    station = window.Station_stat.currentText()
    station = station.split(" ")[0]
    massive = ["Temp", "Humadity", "Precepit", "`Wind speed`", "`Wind direction`"]
    for i in range(len(massive)):
        list_stat = []
        cursor.execute(f"SELECT MIN({massive[i]}) AS minimum FROM weather.measure WHERE Time BETWEEN %s and %s AND id_station = %s ;", (begin_period, end_period, station))
        answer = cursor.fetchone()[0]
        list_stat.append(answer)

        cursor.execute(f"SELECT AVG({massive[i]}) AS average FROM weather.measure WHERE Time BETWEEN %s and %s AND id_station = %s ;", (begin_period, end_period, station))
        answer = cursor.fetchone()[0]
        list_stat.append(answer)

        cursor.execute(f"SELECT MAX({massive[i]}) AS maximum FROM weather.measure WHERE Time BETWEEN %s and %s AND id_station = %s ;", (begin_period, end_period, station))
        answer = cursor.fetchone()[0]
        list_stat.append(answer)

        cursor.execute(f"SELECT VARIANCE({massive[i]}) AS maximum FROM weather.measure WHERE Time BETWEEN %s and %s AND id_station = %s ;", (begin_period, end_period, station))
        answer = cursor.fetchone()[0]
        list_stat.append(answer)

        cursor.execute(f"SELECT STDDEV({massive[i]}) AS maximum FROM weather.measure WHERE Time BETWEEN %s and %s AND id_station = %s ;", (begin_period, end_period, station))
        answer = cursor.fetchone()[0]
        list_stat.append(answer)
        for j in range(len(list_stat)):
            
            font = QFont()
            font.setPointSize(14)
            Item = QTableWidgetItem(str(list_stat[j]))
            Item.setFlags(Item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            Item.setFont(font)
            window.Table_stat.setItem(i, j, Item)
        window.Table_stat.resizeColumnsToContents()
        window.Table_stat.resizeRowsToContents()

def save_to_docx(window):
        create_statistic(window)
        document = Document()
        table = document.add_table(rows=1, cols=window.Table_stat.columnCount())
        
        # Добавление заголовков
        hdr_cells = table.rows[0].cells
        for i in range(window.Table_stat.columnCount()):
            hdr_cells[i].text = window.Table_stat.horizontalHeaderItem(i).text()

        # Добавление данных из QTableWidget
        for row in range(window.Table_stat.rowCount()):
            row_cells = table.add_row().cells
            for col in range(window.Table_stat.columnCount()):
                item = window.Table_stat.item(row, col)
                if item is not None:
                    row_cells[col].text = item.text()
        date = datetime.now()
        date = date.date()
        # Сохранение документа
        document.save(f'./Statistic/Otchet {date}.docx')



def initiliaze_button(window):
    #Окно входа

    #Окно метеоролога
    #Кнопка добавить замер
    window.Add_izm.clicked.connect(lambda: Fill_lineedit_izm(window, 0))
    #Кнопка просмотр статистики
    window.Statitic_view_user.clicked.connect(lambda: fill_combobox(window))

    #Окно администратора
    #Окно управления метеорологами
    window.Emp_view.clicked.connect(lambda :  Fill_table_emp(window))
    #Окно управления станциями
    window.Station_view.clicked.connect(lambda: Fill_table_station(window))
    #Окно управления измерениями
    window.Izm_view.clicked.connect(lambda: Fill_table_measure(window))
    #Окно статистики 
    window.Statistic_view_admin.clicked.connect(lambda: fill_combobox(window))

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
    window.Add_izm_2.clicked.connect(lambda: Fill_lineedit_izm(window, 0))
    window.Red_izm.clicked.connect(lambda: Fill_lineedit_izm(window, 1))
    window.Back_izm.clicked.connect(lambda: change_page(window, starter_page))
    window.Del_izm.clicked.connect(lambda: Remove_measure(window))

    #Окно добавления метеорологов
    window.Back_emp_add.clicked.connect(lambda: Fill_table_emp(window))
    window.Save_emp_add.clicked.connect(lambda: Add_emp(window))

    #Окно добавления станций
    window.Back_station_add.clicked.connect(lambda: Fill_table_station(window))
    window.Save_station_add.clicked.connect(lambda: Add_station(window))

    #Окно добавления измерений
    if starter_page == 1:
        window.Back_izm_add.clicked.connect(lambda: change_page(window, starter_page))
        window.Save_izm_add.clicked.connect(lambda: Add_measure(window))
    else :
        window.Back_izm_add.clicked.connect(lambda: Fill_table_measure(window))
        window.Save_izm_add.clicked.connect(lambda: Add_measure(window))

    #Окно статистики
    if starter_page == 1:
        window.Back_stat.clicked.connect(lambda: change_page(window, starter_page))
    else :
        window.Back_stat.clicked.connect(lambda: change_page(window, 2))
    
    window.Create_stat.clicked.connect(lambda: create_statistic(window))
    window.Save_word_stat.clicked.connect(lambda: save_to_docx(window))

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
