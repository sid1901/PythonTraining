try:
	fh = open("name2.txt","r")
	s=fh.read()
	print(s)
except IOError:
	fh2 = open("name2.txt","w")
	fh2.write("Newly Created")
	print("exception block says dint find the file but created a newone")
else:
	print("written successfully")
	fh.close()