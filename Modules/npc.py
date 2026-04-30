class NPC:
	def __init__(self, npc_type, cart):
		self.npc_type = npc_type
		self.cart = cart

	def __str__(self):
		return (
			f"NPC: {self.npc_type}\n"
			f"Order: \n{self.cart}\n"
		)