from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
  '''
  Main window of the RPN Calculator

  Responsible for reading user input,
  maintaining partially entered values,
  and displaying the stack.
  '''

  def __init__(self):
    super().__init__()

    self.setStyleSheet("""
    * {
      font: bold 18px sans-serif;
    }

    QPushButton#Numpad {
      background-color: #666;
    }

    QPushButton#Numpad::pressed {
      background-color: #777;
    }

    QPushButton#Operator {
      background-color: #066;
    }

    QPushButton#Operator::pressed {
      background-color: #077;
    }
    """)

    frame = QWidget()
    frameLayout = QVBoxLayout(frame)
    self.setCentralWidget(frame)

    displayFrame = QGroupBox()
    displayFrameLayout = QGridLayout(displayFrame)
    frameLayout.addWidget(displayFrame)

    self.stackDisplay = []

    # Stack Display
    for i in range(4):
      displayFrameLayout.addWidget( QLabel( str(i), objectName="Label" ), 3-i, 0 )
      
      display = QLabel( "-", objectName="Display" )
      self.stackDisplay.append(display)
      displayFrameLayout.addWidget( display, 3-i, 1 )

    # Control Buttons
    keypadFrame = QWidget()
    keypadFrameLayout = QGridLayout(keypadFrame)
    frameLayout.addWidget(keypadFrame)

    # Stack Operations
    keypadFrameLayout.addWidget( QPushButton( "Enter", objectName="Operator" ), 0, 2, 1, 2 )

    # Numeric Input
    for i in range(9):
      keypadFrameLayout.addWidget( QPushButton( str(i + 1), objectName="Numpad" ), 2 + i // 3, i % 3 )

    keypadFrameLayout.addWidget( QPushButton( "0", objectName="Numpad" ), 5, 0, 1, 2 )
    keypadFrameLayout.addWidget( QPushButton( ".", objectName="Numpad" ), 5, 2 )

    # Arithmetic operations
    keypadFrameLayout.addWidget( QPushButton( "/", objectName="Operator" ), 2, 3 )
    keypadFrameLayout.addWidget( QPushButton( "*", objectName="Operator" ), 3, 3 )
    keypadFrameLayout.addWidget( QPushButton( "-", objectName="Operator" ), 4, 3 )
    keypadFrameLayout.addWidget( QPushButton( "+", objectName="Operator" ), 5, 3 )

