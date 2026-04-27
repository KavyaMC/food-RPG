from game_logic.business import Business
class Player:
	def __init__(self, name, business_name):
		self.name=name.strip().title()
		self.business=Business(business_name)
		self.coins=250
		self.level=1
		self.experience=0
		self.achievements=set()

	def unlock_achievement(self, achievement_id):
		if achievement_id not in self.achievements:
			self.achievements.add(achievement_id)
			return True
		return False

	def has_achievement(self, achievement_id):
		return achievement_id in self.achievements