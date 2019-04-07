for x in range(20,2000000):
	zmienna = True
	for z in (int(i) for i in str(x)):
		if z%2!=0:
			zmienna = False
	if zmienna  == True:
		print (x)
