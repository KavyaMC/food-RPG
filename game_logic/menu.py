class Menu:
	def __init__(self, title, options):
		self.title=title.upper()
		self.options={}

	def add_option(self, key, text, action):
		self.options["key"]=(text, action)

	def display(self):
		print(f"---{self.title}---")
		for key, (text, _) in self.options.items():
			print(f"{key}. {text}")

	def run(self):
		while True:
			self.display()
			choice=input("Enter a choice: ").strip()
			if choice in self.options:
				action = self.options[choice][1]
				result=action()
				if result=="exit":
					print("Exiting menu")
					input("Press enter to continue")
					break
			else:
				print("invalid choice")

	def exit_menu(self):
		return "exit"