from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from interface import Ui_MainWindow

def change_page(window, num):
    window.stackedWidget.setCurrentIndex(num)

def initiliaze_button(window):
    #Окно метеоролога
    #Кнопка добавить замер
    window.Add_izm.clicked.connect(lambda: change_page(window, 7))
    #Кнопка просмотр статистики
    window.Statitic.clicked.connect(lambda: change_page(window, 8))

    #Окно администратора
    #Окно управления метеорологами
    window.Emp_view.clicked.connect(lambda: change_page(window, 2))
    #Окно управления станциями
    window.Station_view.clicked.connect(lambda: change_page(window, 3))
    #Окно управления измерениями
    window.Izm_view.clicked.connect(lambda: change_page(window, 4))
    #Окно статистики 
    window.Statistic.clicked.connect(lambda: change_page(window, 8))

    #Окно управления пользователями
    window.Add_emp.clicked.connect(lambda: change_page(window, 5))
    window.Redac_emp.clicked.connect(lambda: change_page(window, 5))
    #window.Del_emp.clicked.connect()

    #Окно управления станциями
    window.Add_station.clicked.connect(lambda: change_page(window, 6))
    window.Red_station.clicked.connect(lambda: change_page(window, 6))
    #window.Del_station.clicked.connect()

    #Окно управления измерениями
    window.Add_izm_2.clicked.connect(lambda: change_page(window, 7))
    window.Red_izm.clicked.connect(lambda: change_page(window, 7))
    #window.Del_izm.clicked.connect()

    #Окно добавления метеорологов
    window.Back_emp.clicked.connect(lambda: change_page(window, 2))
    #window.Save_emp.clicked.connect())

    #Окно добавления станций
    window.Back_station.clicked.connect(lambda: change_page(window, 3))
    #window.Back_emp.clicked.connect()

    #Окно добавления измерений
    window.Back_izm.clicked.connect(lambda: change_page(window, 4))
    #window.Save_izm.clicked.connect()

    #Окно статистики
    window.Back_stat.clicked.connect(lambda: change_page(window, 1))
    #window.Create_stat.clicked.connect(lambda: change_page(window, 4))
    #window.Save_stat.clicked.connect(lambda: change_page(window, 4))

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    Content_main_window = Ui_MainWindow()
    Content_main_window.setupUi(main_window)
    initiliaze_button(Content_main_window)
    main_window.show()
    sys.exit(app.exec())
