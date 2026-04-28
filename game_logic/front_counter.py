import os

def show_cafe_menu(menu):
		print("\n===== Café Menu =====")
		for i, (item, price) in enumerate(menu.items(), start=1):
			print(f"{i}. {item} — ₹{price}")
		print("=====================\n")

def load_menu(file_name):
	menu={}
	with open(file_name, "r") as f:
		for line in f:
			line=line.strip()
			if not line:
				continue
			parts=line.split(",")
			item_name=parts[0].strip()
			price=int(parts[1].strip())
			menu[item_name]=price
	return menu


def write_default_menu(file_name):
	default_items=[
		"bread loaf,20",
		"pancake,10",
		"hard boiled egg,6",
		"seasoned egg,8",
		"scrambled egg,10",
		"warm milk,6"
	]
	with open(file_name, "w") as f:
		for item in default_items:
			f.write(item+"\n")
	return "menu reset"


def create_menu_file(file_name):
	if os.path.isfile(file_name):
		try:
			with open(file_name, "r") as f:
				pass
			return f"{file_name} already exists"
		except PermissionError:
			return f"Permission denied reading {file_name}"
	else:
		try:
			with open(file_name, "w") as f:
				f.write("")
			return f"{file_name} created successfully"
		except PermissionError:
			return f"Permission denied creating {file_name}"

def front_counter_menu():
	options=["Show café menu", "Take customer order", "View current order", "Generate bill", "Cancel current order"]
	while True:
		print("---FRONT COUNTER---")
		for index, option in enumerate(options, start=1):
			print(f"{index}: {option}")
		print("0: Return to main menu")
		choice=input("Enter 1-5 or 0 to return: ").strip()
		match choice:
			case "1":
				menu=load_menu("menu.txt")
				show_cafe_menu(menu)

			case "2":
				print(f"{options[int(choice)-1]} in development")
			case "3":
				print(f"{options[int(choice)-1]} in development")
			case "4":
				print(f"{options[int(choice)-1]} in development")
			case "5":
				print(f"{options[int(choice)-1]} in development")
			case "0":
				print("Returning to main menu")
				break
			case _:
				print("Invalid choice. Please try again.")
