class P(object):
	def __init__(self):
		print("p cons")
	
	def method(self):
		print("P method")


class C(P):
	def __init__(self):
		print("c cons")

	def method(self):
		super(C,self).method()
		print("c method") 


pobj=P()
pobj.method()
obj = C()
obj.method()



class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2