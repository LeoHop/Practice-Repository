class ticket(object):
	"""docstring for ticket"""
	def __init__(self, n, c, d):
		self.number = n
		self.cost = c
		self.days = d

	def __str__(self):
		return "Number: {0}, Price: ${1}".format(self.number, self.cost)

	def get_cost(self):
		return "$" + str(self.cost)
		

class WalkupTicket(ticket):
	"""docstring for WalkupTicket"""
	def __init__(self, n):
		super(WalkupTicket, self).__init__(n, 50, 0)

	def __str__(self):
		return "Number: {0}, Price: ${1}".format(self.number, self.cost)

class AdvanceTicket(ticket):
	"""docstring for AdvanceTicket"""
	def __init__(self, n, d):
		super(AdvanceTicket, self).__init__(n, 40, d)
		if d >= 10:
			self.cost = 30
		else:
			self.cost = 40
	
	def __str__(self):
		return "Number: {0}, Price: ${1}".format(self.number, self.cost)


class StudentAdvanceTicket(ticket):
	"""docstring for StudentAdvanceTicket"""
	def __init__(self, n, d):
		super(StudentAdvanceTicket, self).__init__(n, 20, d)
		if d >= 10:
			self.cost = 15
		else:
			self.cost = 20


	def __str__(self):
		return "Number: {0}, Price: ${1} (ID Required)".format(self.number, self.cost)


		
		


t1 = WalkupTicket(1)
t2 = AdvanceTicket(2, 15)
t3 = StudentAdvanceTicket(3, 5)

print(t1)
print(t2)
print(t3)
print(t1.get_cost())
print(t2.get_cost())
print(t3.get_cost())

		