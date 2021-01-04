st=str(input('Enter the string you want to be reversed: '))
def str_rev():
	if ' ' in st:
		print (' '.join(st.split()[::-1]))
	else:
		print(st[::-1])
	
def palin():
	rev=st[::-1]
	if rev==st:
		print('String is palindrome')
	else:
		print('String not palindrome')
str_rev()
palin()