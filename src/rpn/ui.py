from enum import Enum
from math import isnan

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

from rpn.calc import RpnCalculator

class UiState(Enum):
  Insert = 0
  Edit = 1

class MainWindow(QMainWindow):
  '''
  Main window of the RPN Calculator

  Responsible for reading user input,
  maintaining partially entered values,
  and displaying the stack.
  '''

  def __init__(self):
    super().__init__()

    self.rpn = RpnCalculator()

    self.state = UiState.Insert
    self.value = ''


    if QApplication.styleHints().colorScheme() == Qt.ColorScheme.Light:
      self.setStyleSheet("""
      * {
        font: bold 18px sans-serif;
      }

      QPushButton#Numpad {
        background-color: #bbb;
      }

      QPushButton#Numpad::pressed {
        background-color: #aaa;
      }

      QPushButton#Operator {
        background-color: #bbf;
      }

      QPushButton#Operator::pressed {
        background-color: #aad;
      }
      """)
    else:
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
        background-color: #55b;
      }

      QPushButton#Operator::pressed {
        background-color: #66c;
      }
      """)

    frame = QWidget()
    frameLayout = QVBoxLayout(frame)
    self.setCentralWidget(frame)

    displayFrame = QGroupBox()
    displayFrameLayout = QGridLayout(displayFrame)
    displayFrameLayout.setColumnStretch(0,0)
    displayFrameLayout.setColumnStretch(1,1)
    frameLayout.addWidget(displayFrame)

    self.stack_display = []

    # Stack Display
    for i in range(4):
      displayFrameLayout.addWidget( QLabel( str(i), objectName="Label" ), 3-i, 0 )
      
      display = QLabel( "-", objectName="Display" )
      display.setAlignment( Qt.AlignRight )
      self.stack_display.append(display)
      displayFrameLayout.addWidget( display, 3-i, 1 )

    # Control Buttons
    keypadFrame = QWidget()
    keypadFrameLayout = QGridLayout(keypadFrame)
    frameLayout.addWidget(keypadFrame)

    # Stack Operations
    keypadFrameLayout.addWidget( self.make_operator_button( "<-", self.rpn.pop ), 0, 0 )
    keypadFrameLayout.addWidget( self.make_operator_button( "X<>Y", self.rpn.exchange ), 0, 1 )
    keypadFrameLayout.addWidget( self.make_operator_button( "Enter", lambda: None ), 0, 2, 1, 2 )

    # Numeric Input
    for i in range(9):
      button = self.make_numpad_button( str(i + 1) )
      keypadFrameLayout.addWidget( button, 2 + i // 3, i % 3 )

    zeroButton = self.make_numpad_button( '0' )
    keypadFrameLayout.addWidget( zeroButton, 5, 0, 1, 2 )

    keypadFrameLayout.addWidget( self.make_numpad_button( "." ), 5, 2 )

    # Arithmetic operations
    keypadFrameLayout.addWidget( self.make_operator_button("/", self.rpn.div ), 2, 3 )
    keypadFrameLayout.addWidget( self.make_operator_button("*", self.rpn.mul ), 3, 3 )
    keypadFrameLayout.addWidget( self.make_operator_button("-", self.rpn.sub ), 4, 3 )
    keypadFrameLayout.addWidget( self.make_operator_button("+", self.rpn.add ), 5, 3 )

  def make_numpad_button(self, digit):
    '''
    Create a button for numeric input
    '''
    button = QPushButton( digit, objectName="Numpad" )
    button.clicked.connect( lambda: self.add_digit(digit) )
    return button

  def make_operator_button( self, text, func ):
    '''
    Create a button for an operator
    '''
    button = QPushButton( text, objectName="Operator" )
    button.clicked.connect( lambda: self.do_operation(func) )
    return button

  def add_digit(self, d):
    '''
    Add digit to the currently edited number
    '''
    if self.state == UiState.Insert:
      self.state = UiState.Edit
      self.value = d
    else:
      self.value += d
    self.update_display()

  def do_operation(self, func):
    '''
    Run an operation,
    First pushing any edited value onto the stack
    And after updating the display
    '''
    self.push_edit()
    func()
    self.update_display()

  def update_display(self):
    '''
    Update the stack display
    '''
    for i in range(4):
      # In insert mode show the stack as it exists
      # In edit mode show the value being edited as if it were
      # at the top of the stack
      if self.state == UiState.Insert:
        v = self.rpn.peek(i)
      elif i == 0:
        v = self.value
      else:
        v = self.rpn.peek(i - 1)

      if v is None:
        self.stack_display[i].setText( '-' )
      else:
        self.stack_display[i].setText( str(v) )

  def push_edit(self):
    '''
    Push the edited value (if any) onto the stack
    '''
    if self.state == UiState.Edit:
      value = float(self.value)
      self.rpn.push( value )
      self.state = UiState.Insert
