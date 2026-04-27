class Item:
	def __init__(self, name, type, category, meta=None):
		self.name=name.strip()
		self.type=type.strip()
		self.category=category.strip()
		self.meta={}

	def __str__(self):
		return f"item: {self.name}, (category: {self.category})"

	def __repr__(self):
		return f"{self.__class__.__name__}(name={self.name}, category={self.category}, meta={self.meta})"