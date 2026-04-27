from PySide6.QtWidgets import (
	QDialog,
	QVBoxLayout,
	QLabel,
	QLineEdit,
	QPushButton
)


class NewGameWizard(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Welcome to Food RPG")

		layout = QVBoxLayout()
		self.setLayout(layout)

		# Intro text
		intro = QLabel(
			"Welcome to Food RPG.\n"
			"Please enter your details to begin."
		)
		layout.addWidget(intro)

		# Player name
		layout.addWidget(QLabel("Enter player name:"))

		self.player_name_input = QLineEdit()
		self.player_name_input.setPlaceholderText(
			"e.g. Alex"
		)
		self.player_name_input.setAccessibleName("Player name input field")
		layout.addWidget(self.player_name_input)

		# Business name
		layout.addWidget(QLabel("Enter business name:"))
		self.business_name_input = QLineEdit()
		self.business_name_input.setPlaceholderText("e.g. Alex's Kitchen")
		self.business_name_input.setAccessibleName("Business name input field")
		layout.addWidget(self.business_name_input)

		# Create button
		create_btn = QPushButton("Create Game")
		create_btn.clicked.connect(self.accept)

		layout.addWidget(create_btn)

		# UX improvement: start typing immediately
		self.player_name_input.setFocus()