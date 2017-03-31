#Global Scope
b=20  
def msg():  
           a=10  
           print ("Value of a is",a  )
           print ("Value of b is",b  )
           return  
  
msg()  
print (b  )

#----------------------

#Local Scope
def msg2():
	x=1
	print ('x is',x)
	return
msg2()
#print (x) GIVES ErROR x not defined


