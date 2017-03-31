#Function Definition  
def msg(Id,Name,Age=21):  
         "Printing the passed value"  
         print (Id)  
         print (Name  )
         print (Age  )
         return  
#Function call  
msg(Id=100,Name='Ravi',Age=20)  
msg(Id=101,Name='Ratan')  


#-------------------

#Function Definiton  
def square(x):  
    return x*x  

#Calling square function  
print ('\n',"Square of number is",square(10))

#---------------------

#Function Definiton  
square=lambda x: x*x  
  
#Calling square as a function  
print ('\n',"Square of number is",square(10) )

#-------------------------


