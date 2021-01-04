def calc(a,b,c):
	if c not in '+-*/':
		return 'Please enter from +,-,*,/'
	if c=='+':
		return(str(a)+' '+c+' '+str(b)+' = '+str(a+b))
	elif c=='-':
		return(str(a)+' '+c+' '+str(b)+' = '+str(a-b))
	elif c=='*':
		return(str(a)+' '+c+' '+str(b)+' = '+str(a*b))
	elif c=='/':
		return(str(a)+' '+c+' '+str(b)+' = '+str(a/b))

def solve(): #wrapper class
	a=int(input('Please type 1st number:'))
	b=int(input('Please type 2nd number:'))
	c=input('What operation would you like to do? \n Choose between: "+,-,*,/')
	print(calc(a,b,c))

solve()

