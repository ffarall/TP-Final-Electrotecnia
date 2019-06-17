from InterfazGráfica.GUI import ElectroGUI
from Grapher.FiltersGrapher import FiltersGrapher
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
qt_app = ElectroGUI()
qt_app.show()
sys.exit(app.exec_())

