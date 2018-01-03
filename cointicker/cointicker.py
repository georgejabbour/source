import sys
import coinhelpers
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow): 
	def __init__(self): #initial thing that runs every time we make a window object, like a template
		super(Window, self).__init__()
		self.setGeometry(50,50,300,300)
		self.setWindowTitle("CoinTicker")
		self.setWindowIcon(QtGui.QIcon('bitcoin48.png'))

		coin_names = coinhelpers.get_coin_names()

		self.coinChoice = QtGui.QLabel("choose a coin", self)
		comboBox = QtGui.QComboBox(self)
		comboBox.addItems(coin_names)
		
		comboBox.move(50,250)
		self.coinChoice.move(50,50)

		comboBox.activated[str].connect(self.coin_choice)

		self.show()


	def coin_choice(self, text):
		self.coinChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

	def close_application(self): #custom quitting method
		sys.exit()

	#this makes the window exit button use our exit method instead
	def closeEvent(self, event):
		event.ignore()
		self.close_application()


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()