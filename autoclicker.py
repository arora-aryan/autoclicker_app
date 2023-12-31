from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont
from pynput import mouse
import pyautogui
import time

class DrawingMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dots = []
        self.click_positions = []  # Store click positions
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Screen Filling Window")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowOpacity(0.50)

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        self.showMaximized()

        label = QLabel("Execute your click pattern", container)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont('Arial', 20))
        layout.addWidget(label)

        # Button layout for "Done" and "Reset" buttons
        button_layout = QHBoxLayout()

        reset_button = QPushButton("Reset", container)
        reset_button.setFont(QFont('Arial', 16))
        reset_button.clicked.connect(self.resetDrawing)
        button_layout.addWidget(reset_button)

        done_button = QPushButton("Done", container)
        done_button.setFont(QFont('Arial', 16))
        done_button.clicked.connect(self.executeClickPattern)
        button_layout.addWidget(done_button)

        layout.addLayout(button_layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dots.append(event.pos())
            self.update()
            mouse_position = pyautogui.position()
            self.click_positions.append(mouse_position)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor('green')))
        for dot in self.dots:
            mapped_dot = self.centralWidget().mapFromParent(dot)
            painter.drawEllipse(mapped_dot, 5, 5)

    def resetDrawing(self):
        self.dots = []
        self.click_positions = []
        self.update()

    def executeClickPattern(self):
        self.showMinimized()  # Minimize the window
        QTimer.singleShot(1000, self.move_mouse)  # Wait for 1000 ms (1 second) then execute move_mouse


    def move_mouse(self):
        time.sleep(3)  # Small delay to minimize the window before starting the clicks
        for pos in self.click_positions:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
            time.sleep(0.5)  # Adjust time delay as needed
        print("Click pattern executed.")

if __name__ == "__main__":
    app = QApplication([])
    main_window = DrawingMainWindow()
    main_window.show()
    app.exec_()
