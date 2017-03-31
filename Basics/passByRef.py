#Pass by reference

def fun_list(l):
	l[2]=100
	return
l2=[1,2,3]
print('before fun',l2)
fun_list(l2)
print('after fun',l2)

#------------


def fun2_list(l):
	l=['a','b','c']
	return
l2=[1,2,3]
print('before fun',l2)
fun2_list(l2)
print('after fun',l2)
