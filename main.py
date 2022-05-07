
from PyQt5.QtWidgets import QApplication,  QWidget
import sys

from ATM.Form import m_Form

if __name__ == '__main__':
      app = QApplication(sys.argv)

      w = QWidget()
      gw = m_Form(w)
      w.show()

      sys.exit(app.exec_())
