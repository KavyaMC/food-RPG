import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Food Tykoon RPG")
		self.setAccessibleName(f"{self.WindowTitle()} - main window")

def main():
	app=QApplication(sys.argv)
	window=MainWindow()
	window.show()
	sys.exit(app.exec())

if __name__=="__main__":
	main()