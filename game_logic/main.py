from cafe_menu import cafe_menu
from front_counter import create_menu_file, write_default_menu
if __name__ == "__main__":
	print(create_menu_file("menu.txt"))
	write_default_menu("menu.txt")

	cafe_menu()