from inventory import has_item, remove_item, add_item

def craft(recipe):
	ingredients = recipe["inputs"]
	output = recipe["outputs"]
	for item, amount in ingredients.items():
		if not has_item(item, amount):
			print(f"Missing: {item}")
			return False
	for item, amount in ingredients.items():
		remove_item(item, amount)
	for item, amount in output.items():
		add_item(item, amount)
		print(f"Crafted: {output}")
	return True