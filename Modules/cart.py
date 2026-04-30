from .order import Order
class Cart:
	def __init__(self):
		self.orders=[]

	def add_order(self, order):
		self.orders.append(order)

	def total_cost(self):
		for order in self.orders:
			return sum(order.total_price())

	def __str__(self):
		lines=[]
		for order in self.orders:
			lines.append(str(order))
		lines.append(f"Cart Total: {self.total_cost()} coins")
		return "\n".join(lines)