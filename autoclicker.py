from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont

class DrawingMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dots = []
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
        done_button.clicked.connect(self.showMinimized)
        button_layout.addWidget(done_button)

        layout.addLayout(button_layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dots.append(event.pos())
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor('green')))
        for dot in self.dots:
            mapped_dot = self.centralWidget().mapFromParent(dot)
            painter.drawEllipse(mapped_dot, 5, 5)

    def resetDrawing(self):
        self.dots = []
        self.update()

if __name__ == "__main__":
    app = QApplication([])
    main_window = DrawingMainWindow()
    main_window.show()
    app.exec_()

#this is exactly how i want my window to function lol nice



