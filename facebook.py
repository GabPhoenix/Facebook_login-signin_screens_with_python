from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #call left frame
        self.left()

        #call right frame
        self.right()

    def left(self):
        self.frame_left = QFrame(self)
        self.frame_left.setGeometry(0, 0, 400, 600)
        self.frame_left.setStyleSheet(
            "QFrame{"
                "background-color: #fff;"
                "border-radius: 15px;"
            "}"
        )
        
        # Label icon/image 
        icon_facebook = QIcon('facebook.png')
        pixmap1 = icon_facebook.pixmap(150, 150, QIcon.Active)

        self.label = QLabel(self.frame_left)
        self.label.setGeometry(125, 150, 150, 150)
        self.label.setPixmap(pixmap1)

        # Label name
        self.label_name = QLabel(self.frame_left)
        self.label_name.setGeometry(50, 300, 400, 100)
        self.label_name.setText("facebook")
        self.label_name.setStyleSheet(
            "QLabel{"
                "background-color: transparent;"
                "color: #1878F2;"
                "font: 60pt \"Tw Cen MT\";"
            "}"
        )


    def right(self):
        self.frame_right = QFrame(self)
        self.frame_right.setGeometry(400, 15, 400, 570)
        self.frame_right.setStyleSheet(
            "background-color: #1878F2;"
            "border-top-right-radius: 15px;"
            "border-bottom-right-radius: 15px;"
        )

        #close button
        self.close = QPushButton(self.frame_right)
        self.close.setGeometry(360, 15, 25, 25)
        self.close.setCursor(Qt.PointingHandCursor)
        self.close.setText("X")
        self.close.clicked.connect(self.close_window)
        self.close.setStyleSheet(
            "QPushButton{"
                "border-radius: 12px;"
                "background-color: #fff;"
                "color: #fff;"
                "font: 21pt \"Tw Cen MT\";"
            "}"
            "QPushButton:hover{"
                "color: #1878F2;"
            "}"
        )

        #Name "login"
        self.login = QLabel(self.frame_right)
        self.login.setGeometry(130, 100, 400, 70)
        self.login.setText("Login")
        self.login.setStyleSheet(
            "QLabel{"
                "background-color: transparent;"
                "color: #fff;"
                "font: 45pt \"Tw Cen MT\";"
            "}"
        )

        #Entries
        self.username = QLineEdit(self.frame_right)
        self.username.setGeometry(30, 190, 340, 50)
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet(
            "QLineEdit{"
                "background-color: #b6cff2;"
                "border-radius: 12px;"
                "color:  #1878F2;"
                "font: 17pt \"Tw Cen MT\";"
            "}"
            "QLineEdit:hover{"
                "border: 2px solid #000;"
            "}"
        )

        self.password = QLineEdit(self.frame_right)
        self.password.setGeometry(30, 260, 340, 50)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(
            "QLineEdit{"
                "background-color: #b6cff2;"
                "border-radius: 12px;"
                "color:  #1878F2;"
                "font: 17pt \"Tw Cen MT\";"
            "}"
            "QLineEdit:hover{"
                "border: 2px solid #000;"
            "}"
        )

        self.go_button = QPushButton(self.frame_right)
        self.go_button.setGeometry(120, 350, 150, 50)
        self.go_button.setCursor(Qt.PointingHandCursor)
        self.go_button.setText("Login")
        self.go_button.setStyleSheet(
            "QPushButton{"
                "background-color: #fff;"
                "color: #1878F2;"
                "border-radius: 12px;"
                "font: 18pt \"Tw Cen Mt\";"
            "}"
            "QPushButton:hover{"
                "background-color: #1878F2;"
                "color: #fff;"
                "border: 2px solid #fff;"
            "}"
        )

        #signin
        self.signup = QPushButton(self.frame_right)
        self.signup.setGeometry(100, 420, 200, 50)
        self.signup.setText("Don't have an account? Sign up!")
        self.signup.setCursor(Qt.PointingHandCursor) 
        self.signup.setStyleSheet(
            "background-color: transparent;"
            "color: #fff;"
            "font: 12pt \"Tw Cen Mt\";"
            "border: none;"
        )
        self.signup.clicked.connect(self.switch)

    def close_window(self):
        sys.exit(MainWindow)
    

    def switch(self):
        self.screen = MainWindow()
        self.screen_login = MainWindow2()
        self.screen_login.show()
        self.screen.hide()

class MainWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #call left frame
        self.left()

        #call right frame
        self.right()

    def right(self):
        self.frame_right = QFrame(self)
        self.frame_right.setGeometry(400, 15, 400, 570)
        self.frame_right.setStyleSheet(
            "QFrame{"
                "background-color: #fff;"
                "border-top-right-radius: 15px;"
                "border-bottom-right-radius: 15px;"
            "}"
        )
        
        # Label icon/image 
        icon_facebook = QIcon('facebook.png')
        pixmap1 = icon_facebook.pixmap(150, 150, QIcon.Active)

        self.label = QLabel(self.frame_right)
        self.label.setGeometry(125, 150, 150, 150)
        self.label.setPixmap(pixmap1)

        # Label name
        self.label_name = QLabel(self.frame_right)
        self.label_name.setGeometry(50, 300, 400, 100)
        self.label_name.setText("facebook")
        self.label_name.setStyleSheet(
            "QLabel{"
                "background-color: transparent;"
                "color: #1878F2;"
                "font: 60pt \"Tw Cen MT\";"
            "}"
        )


    def left(self):
        self.frame_left = QFrame(self)
        self.frame_left.setGeometry(0, 0, 400, 600)
        self.frame_left.setStyleSheet(
            "background-color: #1878F2;"
            "border-radius: 15px;"
        )

        #close button
        self.close = QPushButton(self.frame_left)
        self.close.setGeometry(15, 15, 25, 25)
        self.close.setCursor(Qt.PointingHandCursor)
        self.close.setText("X")
        self.close.clicked.connect(self.close_window)
        self.close.setStyleSheet(
            "QPushButton{"
                "border-radius: 12px;"
                "background-color: #fff;"
                "color: #fff;"
                "font: 21pt \"Tw Cen MT\";"
            "}"
            "QPushButton:hover{"
                "color: #1878F2;"
            "}"
        )

        #Name "Sign in"
        self.sgni = QLabel(self.frame_left)
        self.sgni.setGeometry(120, 100, 400, 70)
        self.sgni.setText("Sign in")
        self.sgni.setStyleSheet(
            "QLabel{"
                "background-color: transparent;"
                "color: #fff;"
                "font: 45pt \"Tw Cen MT\";"
            "}"
        )

        #Entries
        self.username = QLineEdit(self.frame_left)
        self.username.setGeometry(30, 190, 340, 50)
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet(
            "QLineEdit{"
                "background-color: #b6cff2;"
                "border-radius: 12px;"
                "color:  #1878F2;"
                "font: 17pt \"Tw Cen MT\";"
            "}"
            "QLineEdit:hover{"
                "border: 2px solid #000;"
            "}"
        )

        self.email = QLineEdit(self.frame_left)
        self.email.setGeometry(30, 260, 340, 50)
        self.email.setPlaceholderText("Email")
        self.email.setStyleSheet(
            "QLineEdit{"
                "background-color: #b6cff2;"
                "border-radius: 12px;"
                "color:  #1878F2;"
                "font: 17pt \"Tw Cen MT\";"
            "}"
            "QLineEdit:hover{"
                "border: 2px solid #000;"
            "}"
        )


        self.password = QLineEdit(self.frame_left)
        self.password.setGeometry(30, 330, 340, 50)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(
            "QLineEdit{"
                "background-color: #b6cff2;"
                "border-radius: 12px;"
                "color:  #1878F2;"
                "font: 17pt \"Tw Cen MT\";"
            "}"
            "QLineEdit:hover{"
                "border: 2px solid #000;"
            "}"
        )

        self.go_button = QPushButton(self.frame_left)
        self.go_button.setGeometry(120, 420, 150, 50)
        self.go_button.setCursor(Qt.PointingHandCursor)
        self.go_button.setText("Login")
        self.go_button.setStyleSheet(
            "QPushButton{"
                "background-color: #fff;"
                "color: #1878F2;"
                "border-radius: 12px;"
                "font: 18pt \"Tw Cen Mt\";"
            "}"
            "QPushButton:hover{"
                "background-color: #1878F2;"
                "color: #fff;"
                "border: 2px solid #fff;"
            "}"
        )

        #signin
        self.signup = QPushButton(self.frame_left)
        self.signup.setGeometry(90, 480, 220, 50)
        self.signup.setText("Already have an account? Login!")
        self.signup.setCursor(Qt.PointingHandCursor) 
        self.signup.setStyleSheet(
            "background-color: transparent;"
            "color: #fff;"
            "font: 12pt \"Tw Cen Mt\";"
            "border: none;"
        )
        self.signup.clicked.connect(self.switch)

    def switch(self):
        self.screen = MainWindow2()
        self.screen_login = MainWindow()
        self.screen_login.show()
        self.screen.hide()

    def close_window(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit(0)