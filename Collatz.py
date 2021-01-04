def collatz():
	n=int(input('Enter n: '))
	steps=0
	while n!=1:
		if int(n)%2==0:
			n=int(n)/2
			steps=steps+1
		else:
			n=3*int(n)+1
			steps=steps+1
	print('Steps: '+str(steps))
collatz()