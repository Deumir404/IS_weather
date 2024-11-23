from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from interface1 import Ui_MainWindow

def change_page(window, num):
    window.stackedWidget.setCurrentIndex(num)

def auth_user(window):
    global starter_page
    if window.login.text() == "admin" and window.password.text() == "admin":
        change_page(window, 2)
        starter_page = 2
        initiliaze_button(window)
    elif window.login.text() == "user" and window.password.text() == "user":
        change_page(window, 1)
        starter_page = 1
        initiliaze_button(window)
    else :
        window.label_21.setText("Невереный пароль")
        window.label_21.setStyleSheet("color : red")
        

def initiliaze_button(window):
    #Окно входа
    window.Login_b.clicked.connect(lambda :  auth_user(window))

    #Окно метеоролога
    #Кнопка добавить замер
    window.Add_izm.clicked.connect(lambda: change_page(window, 8))
    #Кнопка просмотр статистики
    window.Statitic_view_user.clicked.connect(lambda: change_page(window, 9))

    #Окно администратора
    #Окно управления метеорологами
    window.Emp_view.clicked.connect(lambda: change_page(window, 3))
    #Окно управления станциями
    window.Station_view.clicked.connect(lambda: change_page(window, 4))
    #Окно управления измерениями
    window.Izm_view.clicked.connect(lambda: change_page(window, 5))
    #Окно статистики 
    window.Statistic_view_admin.clicked.connect(lambda: change_page(window, 9))

    #Окно управления пользователями
    window.Add_emp.clicked.connect(lambda: change_page(window, 6))
    window.Redac_emp.clicked.connect(lambda: change_page(window, 6))
    window.Back_emp.clicked.connect(lambda: change_page(window, starter_page))
    #window.Del_emp.clicked.connect()

    #Окно управления станциями
    window.Add_station.clicked.connect(lambda: change_page(window, 7))
    window.Red_station.clicked.connect(lambda: change_page(window, 7))
    window.Back_station.clicked.connect(lambda: change_page(window, starter_page))
    #window.Del_station.clicked.connect()

    #Окно управления измерениями
    window.Add_izm_2.clicked.connect(lambda: change_page(window, 8))
    window.Red_izm.clicked.connect(lambda: change_page(window, 8))
    window.Back_izm.clicked.connect(lambda: change_page(window, starter_page))
    #window.Del_izm.clicked.connect()

    #Окно добавления метеорологов
    window.Back_emp_add.clicked.connect(lambda: change_page(window, 3))
    #window.Save_emp_add.clicked.connect())

    #Окно добавления станций
    window.Back_station_add.clicked.connect(lambda: change_page(window, 4))
    #window.Save_station_add.clicked.connect())

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
    Content_main_window = Ui_MainWindow()
    Content_main_window.setupUi(main_window)
    global starter_page
    starter_page = 0
    initiliaze_button(Content_main_window)
    main_window.show()
    
    sys.exit(app.exec())
