#Write and Read
print('Writing a file')
obj=open("abcd.txt","w")  
obj.write("Welcome to the world of Python")  
obj.close()  
print('Reading a file')
obj1=open("abcd.txt","r")  
s=obj1.read()  
print (s)
obj1.close()  
print('Reading 20 characters from file')
obj2=open("abcd.txt","r")  
s1=obj2.read(20)  
print (s1)  
obj2.close()  


#Setting the position
# Open a file
print('Reading a file')
fo = open("abcd.txt", "r+")
str = fo.read(10);
print ("Read String is : ", str)

print('Cursor Position')
# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
print('Repositioning')
position = fo.seek(5, 0); #offset,from
position = fo.tell();
print ("New file position : ", position)

str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()