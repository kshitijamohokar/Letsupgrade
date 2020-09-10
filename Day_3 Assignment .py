Question 1 >>>

value = int(input("Enter the alltitude"))
if value <= 1000:
   print("Safe to Land") 
elif value > 1000 and value<=5000:
   print("Bring Down To 1000") 
else:
   print("Turn Around ")

Question 2 >>>

for num in range(1 , 201):
	flag = True
	for i in range(2 , (num//2+1)):
		if num%i ==0:
			flag =False
			break
			
	if flag == True:
		print(num)
		
