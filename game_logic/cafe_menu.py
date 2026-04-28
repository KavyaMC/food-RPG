from front_counter import front_counter_menu
def cafe_menu():
	options=["Front Counter", "Chef's Kitchen", "Reception Desk", "Periodic Sales Report", "Shopping App", "End Day"]
	while True:
		print("---Cafe Simulator---")
		for index, option in enumerate(options, start=1):
			print(f"{index}: {option}")
		print("0: exit")
		choice=input("Enter 1-6 or 0 to exit: ").strip()
		match choice:
			case "1":
				front_counter_menu()
			case "2":
				print(f"{options[int(choice)-1]} in development")
			case "3":
				print(f"{options[int(choice)-1]} in development")
			case "4":
				print(f"{options[int(choice)-1]} in development")
			case "5":
				print(f"{options[int(choice)-1]} in development")
			case "6":
				print(f"{options[int(choice)-1]} in development")
			case "0":
				print("Thanks for playing. Exiting program")
				break
			case _:
				print("Invalid choice. Please try again.")