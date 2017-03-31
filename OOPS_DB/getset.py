class Getset:

	def __init__(self,var):
		self.var=var;

	def getvar(self):
		return self.var

	def setvar(self,var):
		self.var=var	

	
obj = Getset(10);
x=obj.getvar();
print("got var as : ",x)
obj.setvar(20);
x=obj.getvar();
print("got var as : ",x)


setattr(obj,"var",50)
print("got var as : ",getattr(obj,"var"))

print(hasattr(obj,"var"))
print(hasattr(obj,"var2"))
setattr(obj,"var3",50)
delattr(obj,"var3")