appliances = {}

def add_appliance(name, amount=1):
	appliances[name] = appliances.get(name, 0) + amount

def remove_appliance(name, amount=1):
	if appliances.get(name, 0) >= amount:
		appliances[name] -= amount

		if appliances[name] == 0:
			del appliances[name]

		return True

	return False

def has_appliance(name, amount=1):
	return appliances.get(name, 0) >= amount