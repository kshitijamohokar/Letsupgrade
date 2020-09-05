for num in range(1 , 201):
	flag = True
	for i in range(2 , (num//2+1)):
		if num%i ==0:
			flag =False
			break
			
	if flag == True:
		print(num)
		