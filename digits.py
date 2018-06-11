i = input()
i = int(i)
count = 0
def countj(i):
	global count
	while(i>0):
		count = count+1
		i =int(i /10)
		 
	return count
count = countj(i)
print(count)
