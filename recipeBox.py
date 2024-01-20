
import sys
import PyQt5.QtWidgets
import PyQt5.QtCore

def main():

    app = PyQt5.QtWidgets.QApplication(sys.argv)

    suggest_button = PyQt5.QtWidgets.QPushButton('Suggest some recipes')
    show_button = PyQt5.QtWidgets.QPushButton('Show me a specific recipe')
    add_button = PyQt5.QtWidgets.QPushButton('Add a recipe')

    def suggest_button_slot():
        suggest_button = PyQt5.QtWidgets.QPushButton('Suggest some recipes')
        show_button = PyQt5.QtWidgets.QPushButton('Show me a specific recipe')

        layout = PyQt5.QtWidgets.QHBoxLayout()
        layout.addWidget(suggest_button)
        layout.addWidget(show_button)

        frame = PyQt5.QtWidgets.QFrame()
        frame.setLayout(layout)

        window = PyQt5.QtWidgets.QMainWindow()
        window.setCentralWidget(frame)
        screen_size = PyQt5.QtWidgets.QDesktopWidget().screenGeometry()
        window.resize(screen_size.width()//2, screen_size.height()//2)
        window.setWindowTitle('Suggest a recipe')
        window.show()

    def show_button_slot():
        layout = PyQt5.QtWidgets.QHBoxLayout()
        layout.addWidget(suggest_button)
        layout.addWidget(show_button)
        layout.addWidget(add_button)

        frame = PyQt5.QtWidgets.QFrame()
        frame.setLayout(layout)

        window = PyQt5.QtWidgets.QMainWindow()
        window.setCentralWidget(frame)
        screen_size = PyQt5.QtWidgets.QDesktopWidget().screenGeometry()
        window.resize(screen_size.width()//2, screen_size.height()//2)
        window.setWindowTitle('Display a recipe')
        window.show()

    def add_button_slot():
        layout = PyQt5.QtWidgets.QHBoxLayout()
        layout.addWidget(suggest_button)
        layout.addWidget(show_button)
        layout.addWidget(add_button)

        frame = PyQt5.QtWidgets.QFrame()
        frame.setLayout(layout)

        window = PyQt5.QtWidgets.QMainWindow()
        window.setCentralWidget(frame)
        screen_size = PyQt5.QtWidgets.QDesktopWidget().screenGeometry()
        window.resize(screen_size.width()//2, screen_size.height()//2)
        window.setWindowTitle('Add a recipe')
        window.show()

    suggest_button.clicked.connect(suggest_button_slot)
    show_button.clicked.connect(show_button_slot)
    add_button.clicked.connect(add_button_slot)

    layout = PyQt5.QtWidgets.QHBoxLayout()
    layout.addWidget(suggest_button)
    layout.addWidget(show_button)
    layout.addWidget(add_button)

    frame = PyQt5.QtWidgets.QFrame()
    frame.setLayout(layout)

    window = PyQt5.QtWidgets.QMainWindow()
    window.setCentralWidget(frame)
    screen_size = PyQt5.QtWidgets.QDesktopWidget().screenGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)
    window.setWindowTitle('Recipe Box')
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
