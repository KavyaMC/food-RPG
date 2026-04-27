class Business:
	def __init__(self, name):
		self.name = name.strip().title()
		self.reputation = 0
		self.business_type = "Restaurant"
		self.is_chain = False