import sys
from PySide6.QtWidgets import QApplication
from rpn.ui import MainWindow

def main():
  QApplication.setApplicationName("Calculator")
  QApplication.setOrganizationName("CPSC-428")
  QApplication.setApplicationVersion("0.1.0")

  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  app.exec()

if __name__ == "__main__":
    main()
