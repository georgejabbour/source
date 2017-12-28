import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(100, 100, 500, 300)
window.setWindowTitle("PyQt!")
window.show()
sys.exit(app.exec_())