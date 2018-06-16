n = input()
k = input()
list1 = []
sum1 = 0
for x in range(0,n):
    num = input()
    list1.append(num)
for i in range(0,k):
    sum1 = sum1+list1[i]
print sum1
