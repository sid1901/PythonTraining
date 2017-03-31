name="Siddharth"  
length=len(name)  
i=0  
for n in range(-1,(-length-1),-1):  #range(-1,-10,-1)
    print (name[i],"\t",name[n])
    i+=1  


print("\n","Range usage","\n")
for m in range(0,9,+1):
    print (name[m])


print('\n','String replication')
print ('sid'*5)
print (5*"sid")


print('\n','Membership op')
str = "sid"
str2 = "SI"
str3 = "si"
print(str2 in str)
print(str3 in str)

print('\n','Relational op')
print('abc' > 'aac')



print('\n','String slicing notation')
str="Nikhil"  
print(str[0:6]  )
print(str[0:3]  )
print(str[2:5]  )
print(str[:3]   )
print(str[3:]	)
