mystr = str(raw_input())
mystr1 = mystr[::-1]
import re
print (re.sub("e|i|o|u|a|A|E|I|O|U", "", mystr1))
