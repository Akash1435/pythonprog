n = input()
list1 = [int(d) for d in str(n)]
l = len (list1)
sum =0
for x in range (0,l):
    sum = sum + (list1[x]**2)
print (sum)
