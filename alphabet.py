char = raw_input('enter something')
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for item in list:
	if(char==item):
		ab=1
		break
	else:
		ab=0
if(ab==1):
	print '\nalphabet'
else:
	print '\nnot an alphabet'