class A:
	
	Count = 0 			#static var/ class var	
	def meth(self):
		x=0			#Local var
		print ("HELOO")
		return

obj = A();
obj.meth();

setattr(obj,'name','Sachin');   	# Creating instance var

print("name",getattr(obj,"name"))
