from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


def show_splash(app):
    splash = QSplashScreen(QPixmap('assets/splash.png'))
    splash.show()

    app.processEvents()
