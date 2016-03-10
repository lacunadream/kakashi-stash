# class lol(object):

# 	def __init__(self, name):
# 		self.name = name

# 	def kay(self):
# 		print('asd')

# 	def kk(self):
# 		print(self.name)


# a = lol('yourmom')
# a.kk()

# class Employee:
#    'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print(Employee.empCount)

#    def displayEmployee(self):
#       print(self.name, self.salary)

# "This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)

# function closures remembered at run time. Evaluate again = evaluate the returned
# def o(kkk):
# 	k = 123
# 	def i():
# 		print('lol')
# 	def ii():
# 		print(kkk)
# 	return ii
# 	print(123)
# 	return i

# k = o(5)
# k()

class x(object):

	def __init__(self, name, steam):
		self.name = name
		self.steam = steam
	
	def fuckyou(self, name):
		print('fuck you', self.name, 'from', name)

	def __repr__(self):
		return self.name

	def __str__(self):
		return 'zz ' + self.name

k = x('siew', 123)
print(k.fuckyou('david'))
print(repr(k))
print(str(k))

class y(x):
	def __str__(self):
		return self.name
lol = y('xxx', 8)
print(repr(lol))




