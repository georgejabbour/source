import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow): 
	def __init__(self): #initial thing that runs every time we make a window object, like a template
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("CoinTicker")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

		#creating the quit action
		quitAction = QtGui.QAction("&Exit", self)
		quitAction.setShortcut("Ctrl+Q")
		quitAction.setStatusTip('Leave The App')
		quitAction.triggered.connect(self.close_application)

		self.statusBar()			#not assigned a variable because it's basic
		mainMenu = self.menuBar()	#assigned a variable bc we want to modify it later on
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(quitAction)

		#run home page
		self.home()

	def home(self):
		#add a quitting button
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)

		#adding a button for the toolbar
		extractAction = QtGui.QAction(QtGui.QIcon('refresh.png'), 'Refresh Prices', self)
		extractAction.triggered.connect(self.refresh)
		#creating a toolbar
		self.toolBar = self.addToolBar("Extraction")
		self.toolBar.addAction(extractAction)

		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100,25)
		checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)

		self.styleChoice = QtGui.QLabel("Windows 10", self)
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		
		comboBox.move(50,250)
		self.styleChoice.move(50,150)

		comboBox.activated[str].connect(self.style_choice)

		self.show()

	def style_choice(self, text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))



	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,6000)
		else:
			self.setGeometry(50,50,500,300)


	def close_application(self): #custom quitting method
		sys.exit()
		# adds confirmation button
		# choice = QtGui.QMessageBox.question(self, 'Quit!',
		# 									"Quit?",
		# 									QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		
		# if choice == QtGui.QMessageBox.Yes:
		# 	sys.exit()
		# else:
		# 	pass

	def refresh(self):
		pass

	#this makes the window exit button use our exit method instead
	def closeEvent(self, event):
		event.ignore()
		self.close_application()


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()