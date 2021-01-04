def fib():	
	num_low=int(input('enter lower limit: '))
	num_up=int(input('enter upper limit: '))
	for num in range(num_low,num_up+1):

	    if num % 3 == 0 and num % 5 == 0:
		    print ('FizzBuzz')

	    elif num % 3 == 0:
		    print ('Fizz')

	    elif num % 5 == 0:
		    print ('Buzz')
		    
	    else:
		    print (num)
fib()