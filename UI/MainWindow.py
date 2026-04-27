from PySide6.QtWidgets import (
	QApplication,
	QMainWindow,
	QWidget,
	QVBoxLayout,
	QMessageBox,
	QPushButton,
	QLabel
)
from PySide6.QtCore import Qt, QTimer
from new_game_wizzard import NewGameWizard

import sys


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Food RPG")
		self.setMinimumSize(800, 500)

		# Central widget
		central_widget = QWidget()
		self.setCentralWidget(central_widget)

		# Layout
		self.layout = QVBoxLayout()
		central_widget.setLayout(self.layout)

		# Start Button
		start_btn = QPushButton("Start Game")
		start_btn.setAccessibleDescription("Start a new game. Shortcut key N.")
		start_btn.setShortcut("N")
		start_btn.clicked.connect(self.new_game)

		# Exit Button
		exit_btn = QPushButton("Exit Game")
		exit_btn.setAccessibleDescription("Close the game window.")
		exit_btn.setShortcut("Esc")
		exit_btn.clicked.connect(self.exit_game)

		# Toast / alert label
		self.alert_label = QLabel("")
		self.alert_label.setAlignment(Qt.AlignCenter)
		self.alert_label.setVisible(False)
		self.alert_label.setAccessibleDescription(".... alert!")
		self.alert_label.setFocusPolicy(Qt.StrongFocus)

		# Add widgets
		self.layout.addStretch()
		self.layout.addWidget(start_btn)
		self.layout.addWidget(exit_btn)
		self.layout.addStretch()
		self.layout.addWidget(self.alert_label)

		# Tab order
		self.setTabOrder(start_btn, exit_btn)

		# Initial focus
		start_btn.setFocus()

	# ---------------- ALERT SYSTEM ----------------

	def announce(self, message, duration=2000):
		self.alert_label.setText(message)
		self.alert_label.setAccessibleName(message)
		self.alert_label.setVisible(True)
		self.alert_label.setFocus()
		QTimer.singleShot(duration, self.hide_alert)

	def hide_alert(self):
		self.alert_label.setVisible(False)
		self.setFocus()

	# ---------------- START FLOW ----------------

	def new_game(self):
		self.announce("Starting a new game.")

		QTimer.singleShot(2000, self.show_welcome_dialog)

	def show_welcome_dialog(self):
		dialog = QMessageBox(self)
		dialog.setWindowTitle("Welcome to Food RPG")
		dialog.setText("You will now set up your new game.")
		dialog.setStandardButtons(QMessageBox.Ok)
		dialog.exec()

		# AFTER OK → OPEN WIZARD
		self.open_wizard()

	def open_wizard(self):
		wizard = NewGameWizard()

		if wizard.exec():
			player_name = wizard.player_name_input.text()
			business_name = wizard.business_name_input.text()
			self.finish_setup(player_name, business_name)

	# ---------------- SETUP FINALIZATION ----------------

	def finish_setup(self, player_name, business_name):
		if not player_name.strip():
			self.announce("Player name cannot be empty.")
			return

		if not business_name.strip():
			self.announce("Business name cannot be empty.")
			return

		self.announce(f"Player: {player_name}")
		self.announce(f"Business: {business_name}")
		self.announce("Game setup complete.")

	# ---------------- EXIT ----------------

	def exit_game(self):
		self.announce("Exiting game.")
		QTimer.singleShot(2000, self.close)


# ---------------- RUN APP ----------------

if __name__ == "__main__":

	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())