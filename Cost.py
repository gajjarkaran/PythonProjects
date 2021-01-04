def cost_calc():
	l=float(input('Enter length: '))
	b=float(input('Enter breadth: '))
	#h=float(input('Enter height: '))
	c=float(input('Enter cost to cover tile per unit square: '))
	area=l*b
	cost= l*b*c
	print('Cost to cover',area,'sq.meters =',cost,'Rs')

cost_calc()