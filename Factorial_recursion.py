def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)

n=int(input("Enter your choice: "))
result=fact(n)
print("Factorial of ",n,"=",result)