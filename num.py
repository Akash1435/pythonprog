n = int(input())
num = []
list1 = []
for x in range (0,n):
    num1 = int(raw_input())
    num.append(num1)
for i in set(num):
    list3 = [i,num.count(i)]
    if (num.count(i)>1):
        list1.append(i)
        list1.sort()
if(num.count(i)==1):
    print 'unique'
print ' '.join(str(x) for x in list1)

   
