class Order:
	next_ID=1
	def __init__(self, item, price, quantity):
		self.order_ID = Order.next_ID
		Order.next_ID+=1
		self.item = item
		self.price=float(price)
		self.quantity=int(quantity)

	def total_price(self):
		return self.price * self.quantity

	def __str__(self):
		return (
			f"ID: {self.order_ID}\n"
			f"Order placed: {self.item} x {self.quantity}\n"
			f"price (each): {self.price} coins\n"
			f"total: {self.total_price()} coins"
		)