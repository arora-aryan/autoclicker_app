from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QDoubleSpinBox, QSpinBox
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
        self.setWindowTitle("Autoclicker")
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

        # DoubleSpinBox for setting click interval
        self.click_interval_spinbox = QDoubleSpinBox(container)
        self.click_interval_spinbox.setRange(0, 60)  # Set range from 0 to 60 seconds
        self.click_interval_spinbox.setValue(0.5)    # Set default value to 0.5 seconds
        self.click_interval_spinbox.setSingleStep(0.1) # Increment in steps of 0.1
        layout.addWidget(self.click_interval_spinbox)

        # SpinBox for setting number of repetitions
        self.repeat_spinbox = QSpinBox(container)
        self.repeat_spinbox.setRange(1, 100)  # Set range from 1 to 100 repetitions
        self.repeat_spinbox.setValue(1)       # Set default value to 1 repetition
        layout.addWidget(self.repeat_spinbox)

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
        time.sleep(3)  # Small delay to minimize the window before starting the clicks
        QTimer.singleShot(1000, self.startRepeatingClickPattern)  # Wait for 1000 ms (1 second) then execute startRepeatingClickPattern

    def startRepeatingClickPattern(self):
        repeat_count = self.repeat_spinbox.value()  # Get repetition count
        for _ in range(repeat_count):
            self.move_mouse()

    def move_mouse(self):
        click_interval = self.click_interval_spinbox.value()  # Get value from spinbox
        for pos in self.click_positions:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
            time.sleep(click_interval)  # Use the user-defined click interval
        print("Click pattern executed.")

if __name__ == "__main__":
    app = QApplication([])
    main_window = DrawingMainWindow()
    main_window.show()
    app.exec_()
