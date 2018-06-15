string1 = 'kabali'
l = len(string1)
list1 = list (string1)
n = int(input())
string = []
count = 0
for x in range (0,n):
    getanagram = str(raw_input())
    string.append(getanagram)
for x in range (0,n):
    if (len(string[x])== l):
        list2 = list(string[x])
        list3 = [[i,list2.count(i)] for i in set(list2)]
        if (list3 == [['a', 2], ['i', 1], ['k', 1], ['b', 1], ['l', 1]]):
            count = count+1
print count
