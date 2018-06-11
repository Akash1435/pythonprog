Python 3.4.4rc1 (v3.4.4rc1:04f3f725896c, Dec  6 2015, 16:42:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> i = input('enter a number')
i = int(i)
count = 0
def countj(i):
	print(i)
	global count
	while(i>0):
		count = count+1
		i =int(i /10)
		 
	return count
count = countj(i)
print(count)
