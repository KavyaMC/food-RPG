inventory = {}

def add_item(name, amount=10):
	inventory[name] = inventory.get(name, 0) + amount

def remove_item(name, amount=1):
	if inventory.get(name, 0) >= amount:
		inventory[name] -= amount
		if inventory[name] == 0:
			del inventory[name]
		return True
	return False

def has_item(name, amount=10):
	return inventory.get(name, 0) >= amount

