def fibseq(n):
	assert n>0
	series=[1]
	while len(series)<n:
		if len(series)==1:
			series.append(1)
		else:
			series.append(series[-1]+series[-2])

	for i in range(len(series)): #numbers to strings
		series[i]=str(series[i])

	return(', '.join(series))

def main():
	print(fibseq(int(input('How many numbers do you want? '))))

if __name__=='__main__':
	main()