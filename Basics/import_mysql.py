class Employee:

	def __init__(self,name,designation):
		self.name = name;
		self.designation=designation;
	
	def display(self):
		a=90;
		print(a);
		print("name is : ",self.name)
		print('designation is : ",self.designation)


emp2 = Employee("Sachin","Developer");
emp2.display();