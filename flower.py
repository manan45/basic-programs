class Flower():
	def __init__(self, flower_name, petals, price):
		self.flower_name = flower_name
		self.petals = petals
		self.price = price

	def name_of_flower(self):
		return self.flower_name
	def number_of_petals(self):
		return self.petals
	def price(self):
		return self.price


Flower = Flower('rose',12,123).price()

print(Flower)

		