import sys
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from app.main_window import MainWindow
from app.splash import show_splash


def main():
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='dark_teal.xml')

    show_splash(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
