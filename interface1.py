# Form implementation generated from reading ui file '111.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Login_menu = QtWidgets.QWidget()
        self.Login_menu.setObjectName("Login_menu")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Login_menu)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_19 = QtWidgets.QLabel(parent=self.Login_menu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_14.addWidget(self.label_19)
        self.login_line = QtWidgets.QLineEdit(parent=self.Login_menu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_line.setFont(font)
        self.login_line.setObjectName("login_line")
        self.verticalLayout_14.addWidget(self.login_line)
        self.label_20 = QtWidgets.QLabel(parent=self.Login_menu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_14.addWidget(self.label_20)
        self.password_line = QtWidgets.QLineEdit(parent=self.Login_menu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_line.setFont(font)
        self.password_line.setObjectName("password_line")
        self.verticalLayout_14.addWidget(self.password_line)
        self.label_21 = QtWidgets.QLabel(parent=self.Login_menu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_14.addWidget(self.label_21)
        self.Login_b = QtWidgets.QPushButton(parent=self.Login_menu)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Login_b.setFont(font)
        self.Login_b.setObjectName("Login_b")
        self.verticalLayout_14.addWidget(self.Login_b)
        self.stackedWidget.addWidget(self.Login_menu)
        self.User_main = QtWidgets.QWidget()
        self.User_main.setObjectName("User_main")
        self.page_1_layout = QtWidgets.QVBoxLayout(self.User_main)
        self.page_1_layout.setContentsMargins(50, -1, 50, -1)
        self.page_1_layout.setObjectName("page_1_layout")
        self.Add_izm = QtWidgets.QPushButton(parent=self.User_main)
        self.Add_izm.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Add_izm.setFont(font)
        self.Add_izm.setObjectName("Add_izm")
        self.page_1_layout.addWidget(self.Add_izm)
        self.Statitic_view_user = QtWidgets.QPushButton(parent=self.User_main)
        self.Statitic_view_user.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Statitic_view_user.setFont(font)
        self.Statitic_view_user.setObjectName("Statitic_view_user")
        self.page_1_layout.addWidget(self.Statitic_view_user)
        self.stackedWidget.addWidget(self.User_main)
        self.Admin_main = QtWidgets.QWidget()
        self.Admin_main.setObjectName("Admin_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Admin_main)
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Emp_view = QtWidgets.QPushButton(parent=self.Admin_main)
        self.Emp_view.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Emp_view.setFont(font)
        self.Emp_view.setObjectName("Emp_view")
        self.verticalLayout.addWidget(self.Emp_view)
        self.Station_view = QtWidgets.QPushButton(parent=self.Admin_main)
        self.Station_view.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Station_view.setFont(font)
        self.Station_view.setObjectName("Station_view")
        self.verticalLayout.addWidget(self.Station_view)
        self.Izm_view = QtWidgets.QPushButton(parent=self.Admin_main)
        self.Izm_view.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Izm_view.setFont(font)
        self.Izm_view.setObjectName("Izm_view")
        self.verticalLayout.addWidget(self.Izm_view)
        self.Statistic_view_admin = QtWidgets.QPushButton(parent=self.Admin_main)
        self.Statistic_view_admin.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Statistic_view_admin.setFont(font)
        self.Statistic_view_admin.setObjectName("Statistic_view_admin")
        self.verticalLayout.addWidget(self.Statistic_view_admin)
        self.stackedWidget.addWidget(self.Admin_main)
        self.Emp_menu = QtWidgets.QWidget()
        self.Emp_menu.setObjectName("Emp_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Emp_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back_emp = QtWidgets.QPushButton(parent=self.Emp_menu)
        self.Back_emp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_emp.setFont(font)
        self.Back_emp.setObjectName("Back_emp")
        self.horizontalLayout_2.addWidget(self.Back_emp)
        self.Add_emp = QtWidgets.QPushButton(parent=self.Emp_menu)
        self.Add_emp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Add_emp.setFont(font)
        self.Add_emp.setObjectName("Add_emp")
        self.horizontalLayout_2.addWidget(self.Add_emp)
        self.Redac_emp = QtWidgets.QPushButton(parent=self.Emp_menu)
        self.Redac_emp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Redac_emp.setFont(font)
        self.Redac_emp.setObjectName("Redac_emp")
        self.horizontalLayout_2.addWidget(self.Redac_emp)
        self.Del_emp = QtWidgets.QPushButton(parent=self.Emp_menu)
        self.Del_emp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Del_emp.setFont(font)
        self.Del_emp.setObjectName("Del_emp")
        self.horizontalLayout_2.addWidget(self.Del_emp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Table_emp = QtWidgets.QTableWidget(parent=self.Emp_menu)
        self.Table_emp.setObjectName("Table_emp")
        self.Table_emp.setColumnCount(0)
        self.Table_emp.setRowCount(0)
        self.verticalLayout_2.addWidget(self.Table_emp)
        self.stackedWidget.addWidget(self.Emp_menu)
        self.Station_menu = QtWidgets.QWidget()
        self.Station_menu.setObjectName("Station_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Station_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back_station = QtWidgets.QPushButton(parent=self.Station_menu)
        self.Back_station.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_station.setFont(font)
        self.Back_station.setObjectName("Back_station")
        self.horizontalLayout.addWidget(self.Back_station)
        self.Add_station = QtWidgets.QPushButton(parent=self.Station_menu)
        self.Add_station.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Add_station.setFont(font)
        self.Add_station.setObjectName("Add_station")
        self.horizontalLayout.addWidget(self.Add_station)
        self.Red_station = QtWidgets.QPushButton(parent=self.Station_menu)
        self.Red_station.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Red_station.setFont(font)
        self.Red_station.setObjectName("Red_station")
        self.horizontalLayout.addWidget(self.Red_station)
        self.Del_station = QtWidgets.QPushButton(parent=self.Station_menu)
        self.Del_station.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Del_station.setFont(font)
        self.Del_station.setObjectName("Del_station")
        self.horizontalLayout.addWidget(self.Del_station)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.Table_station = QtWidgets.QTableWidget(parent=self.Station_menu)
        self.Table_station.setObjectName("Table_station")
        self.Table_station.setColumnCount(0)
        self.Table_station.setRowCount(0)
        self.verticalLayout_3.addWidget(self.Table_station)
        self.stackedWidget.addWidget(self.Station_menu)
        self.Izm_menu = QtWidgets.QWidget()
        self.Izm_menu.setObjectName("Izm_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Izm_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Back_izm = QtWidgets.QPushButton(parent=self.Izm_menu)
        self.Back_izm.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_izm.setFont(font)
        self.Back_izm.setObjectName("Back_izm")
        self.horizontalLayout_3.addWidget(self.Back_izm)
        self.Add_izm_2 = QtWidgets.QPushButton(parent=self.Izm_menu)
        self.Add_izm_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Add_izm_2.setFont(font)
        self.Add_izm_2.setObjectName("Add_izm_2")
        self.horizontalLayout_3.addWidget(self.Add_izm_2)
        self.Red_izm = QtWidgets.QPushButton(parent=self.Izm_menu)
        self.Red_izm.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Red_izm.setFont(font)
        self.Red_izm.setObjectName("Red_izm")
        self.horizontalLayout_3.addWidget(self.Red_izm)
        self.Del_izm = QtWidgets.QPushButton(parent=self.Izm_menu)
        self.Del_izm.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Del_izm.setFont(font)
        self.Del_izm.setObjectName("Del_izm")
        self.horizontalLayout_3.addWidget(self.Del_izm)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_station = QtWidgets.QLabel(parent=self.Izm_menu)
        self.label_station.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_station.setFont(font)
        self.label_station.setObjectName("label_station")
        self.horizontalLayout_5.addWidget(self.label_station)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.Izm_menu)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.Table_izm = QtWidgets.QTableWidget(parent=self.Izm_menu)
        self.Table_izm.setObjectName("Table_izm")
        self.Table_izm.setColumnCount(0)
        self.Table_izm.setRowCount(0)
        self.verticalLayout_5.addWidget(self.Table_izm)
        self.stackedWidget.addWidget(self.Izm_menu)
        self.Emp_add = QtWidgets.QWidget()
        self.Emp_add.setObjectName("Emp_add")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Emp_add)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.Surname = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Surname.setFont(font)
        self.Surname.setObjectName("Surname")
        self.verticalLayout_6.addWidget(self.Surname)
        self.label_2 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.Firstname = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Firstname.setFont(font)
        self.Firstname.setObjectName("Firstname")
        self.verticalLayout_6.addWidget(self.Firstname)
        self.label_3 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.Patronymic = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Patronymic.setFont(font)
        self.Patronymic.setObjectName("Patronymic")
        self.verticalLayout_6.addWidget(self.Patronymic)
        self.label_4 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.Adress = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Adress.setFont(font)
        self.Adress.setObjectName("Adress")
        self.verticalLayout_6.addWidget(self.Adress)
        self.label_5 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.Number = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Number.setFont(font)
        self.Number.setObjectName("Number")
        self.verticalLayout_6.addWidget(self.Number)
        self.label_6 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.Station = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Station.setFont(font)
        self.Station.setObjectName("Station")
        self.verticalLayout_6.addWidget(self.Station)

        self.label_22 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_6.addWidget(self.label_22)

        self.Admin = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Admin.setFont(font)
        self.Admin.setObjectName("Admin")
        self.verticalLayout_6.addWidget(self.Admin)

        self.label_23 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)

        self.Login_line_emp = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Login_line_emp.setFont(font)
        self.Login_line_emp.setObjectName("Login_line_emp")
        self.verticalLayout_6.addWidget(self.Login_line_emp)

        self.label_24 = QtWidgets.QLabel(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_6.addWidget(self.label_24)

        self.Password_line_emp = QtWidgets.QLineEdit(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password_line_emp.setFont(font)
        self.Password_line_emp.setObjectName("Password_line_emp")
        self.verticalLayout_6.addWidget(self.Password_line_emp)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Back_emp_add = QtWidgets.QPushButton(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_emp_add.setFont(font)
        self.Back_emp_add.setObjectName("Back_emp_add")
        self.horizontalLayout_6.addWidget(self.Back_emp_add)
        self.Save_emp_add = QtWidgets.QPushButton(parent=self.Emp_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Save_emp_add.setFont(font)
        self.Save_emp_add.setObjectName("Save_emp_add")
        self.horizontalLayout_6.addWidget(self.Save_emp_add)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.Emp_add)
        self.Station_add = QtWidgets.QWidget()
        self.Station_add.setObjectName("Station_add")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Station_add)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.Station_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.Station_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_7.addWidget(self.lineEdit_8)
        self.label_8 = QtWidgets.QLabel(parent=self.Station_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.Station_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_7.addWidget(self.lineEdit_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Back_station_add = QtWidgets.QPushButton(parent=self.Station_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_station_add.setFont(font)
        self.Back_station_add.setObjectName("Back_station_add")
        self.horizontalLayout_7.addWidget(self.Back_station_add)
        self.Save_station_add = QtWidgets.QPushButton(parent=self.Station_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Save_station_add.setFont(font)
        self.Save_station_add.setObjectName("Save_station_add")
        self.horizontalLayout_7.addWidget(self.Save_station_add)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.Station_add)
        self.Izm_add = QtWidgets.QWidget()
        self.Izm_add.setObjectName("Izm_add")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Izm_add)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_8.addWidget(self.lineEdit_10)
        self.label_10 = QtWidgets.QLabel(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_8.addWidget(self.lineEdit_11)
        self.label_11 = QtWidgets.QLabel(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_8.addWidget(self.lineEdit_12)
        self.label_12 = QtWidgets.QLabel(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_8.addWidget(self.lineEdit_13)
        self.label_13 = QtWidgets.QLabel(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_8.addWidget(self.lineEdit_14)
        self.label_14 = QtWidgets.QLabel(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_8.addWidget(self.lineEdit_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Back_izm_add = QtWidgets.QPushButton(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_izm_add.setFont(font)
        self.Back_izm_add.setObjectName("Back_izm_add")
        self.horizontalLayout_8.addWidget(self.Back_izm_add)
        self.Save_izm_add = QtWidgets.QPushButton(parent=self.Izm_add)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Save_izm_add.setFont(font)
        self.Save_izm_add.setObjectName("Save_izm_add")
        self.horizontalLayout_8.addWidget(self.Save_izm_add)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.Izm_add)
        self.Statistic = QtWidgets.QWidget()
        self.Statistic.setObjectName("Statistic")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Statistic)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(parent=self.Statistic)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_9.addWidget(self.lineEdit_16)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_16 = QtWidgets.QLabel(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.lineEdit_17 = QtWidgets.QLineEdit(parent=self.Statistic)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_10.addWidget(self.lineEdit_17)
        self.horizontalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_17 = QtWidgets.QLabel(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(parent=self.Statistic)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_11.addWidget(self.lineEdit_18)
        self.horizontalLayout_9.addLayout(self.verticalLayout_11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_18 = QtWidgets.QLabel(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_10.addWidget(self.label_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(parent=self.Statistic)
        self.lineEdit_19.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_10.addWidget(self.lineEdit_19)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.Table_stat = QtWidgets.QTableWidget(parent=self.Statistic)
        self.Table_stat.setObjectName("Table_stat")
        self.Table_stat.setColumnCount(0)
        self.Table_stat.setRowCount(0)
        self.verticalLayout_13.addWidget(self.Table_stat)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Back_stat = QtWidgets.QPushButton(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Back_stat.setFont(font)
        self.Back_stat.setObjectName("Back_stat")
        self.horizontalLayout_11.addWidget(self.Back_stat)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Create_stat = QtWidgets.QPushButton(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Create_stat.setFont(font)
        self.Create_stat.setObjectName("Create_stat")
        self.verticalLayout_12.addWidget(self.Create_stat)
        self.Save_word_stat = QtWidgets.QPushButton(parent=self.Statistic)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Save_word_stat.setFont(font)
        self.Save_word_stat.setObjectName("Save_word_stat")
        self.verticalLayout_12.addWidget(self.Save_word_stat)
        self.horizontalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.stackedWidget.addWidget(self.Statistic)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "Логин"))
        self.label_20.setText(_translate("MainWindow", "Пароль"))
        self.Login_b.setText(_translate("MainWindow", "Войти"))
        self.Add_izm.setText(_translate("MainWindow", "Добавить измерение"))
        self.Statitic_view_user.setText(_translate("MainWindow", "Посмотреть статистику"))
        self.Emp_view.setText(_translate("MainWindow", "Управление метеорологами"))
        self.Station_view.setText(_translate("MainWindow", "Управление станциями"))
        self.Izm_view.setText(_translate("MainWindow", "Управление измерениями"))
        self.Statistic_view_admin.setText(_translate("MainWindow", "Посмотреть статистику"))
        self.Back_emp.setText(_translate("MainWindow", "Назад"))
        self.Add_emp.setText(_translate("MainWindow", "Добавить пользователя"))
        self.Redac_emp.setText(_translate("MainWindow", "Редактировать пользователя"))
        self.Del_emp.setText(_translate("MainWindow", "Удалить пользователя"))
        self.Back_station.setText(_translate("MainWindow", "Назад"))
        self.Add_station.setText(_translate("MainWindow", "Добавить станцию"))
        self.Red_station.setText(_translate("MainWindow", "Редактировать станцию"))
        self.Del_station.setText(_translate("MainWindow", "Удалить станцию"))
        self.Back_izm.setText(_translate("MainWindow", "Назад"))
        self.Add_izm_2.setText(_translate("MainWindow", "Добавить измерение"))
        self.Red_izm.setText(_translate("MainWindow", "Редактировать измерение"))
        self.Del_izm.setText(_translate("MainWindow", "Удалить измерение"))
        self.label_station.setText(_translate("MainWindow", "Станция: "))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество(опционально)"))
        self.label_4.setText(_translate("MainWindow", "Адрес"))
        self.label_5.setText(_translate("MainWindow", "Номер телефона"))
        self.label_6.setText(_translate("MainWindow", "Станция"))
        self.Back_emp_add.setText(_translate("MainWindow", "Назад"))
        self.Save_emp_add.setText(_translate("MainWindow", "Сохранить"))
        self.label_7.setText(_translate("MainWindow", "Название"))
        self.label_8.setText(_translate("MainWindow", "Координаты"))
        self.Back_station_add.setText(_translate("MainWindow", "Назад"))
        self.Save_station_add.setText(_translate("MainWindow", "Сохранить"))
        self.label_9.setText(_translate("MainWindow", "Время замера"))
        self.label_10.setText(_translate("MainWindow", "Температура"))
        self.label_11.setText(_translate("MainWindow", "Влажность"))
        self.label_12.setText(_translate("MainWindow", "Осадки"))
        self.label_13.setText(_translate("MainWindow", "Направление ветра"))
        self.label_14.setText(_translate("MainWindow", "Скорость ветра"))
        self.Back_izm_add.setText(_translate("MainWindow", "Назад"))
        self.Save_izm_add.setText(_translate("MainWindow", "Сохранить"))
        self.label_15.setText(_translate("MainWindow", "Начало периода"))
        self.label_16.setText(_translate("MainWindow", "Конец периода"))
        self.label_17.setText(_translate("MainWindow", "Станция"))
        self.label_18.setText(_translate("MainWindow", "Характеристика"))
        self.Back_stat.setText(_translate("MainWindow", "Назад"))
        self.Create_stat.setText(_translate("MainWindow", "Сформировать"))
        self.Save_word_stat.setText(_translate("MainWindow", "Сохранить в .docx"))
        self.label_23.setText(_translate("MainWindow", "Логин для входа"))
        self.label_24.setText(_translate("MainWindow", "Пароль"))
        self.label_22.setText(_translate("MainWindow", "Админ?"))
