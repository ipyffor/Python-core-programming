import re
patt = '[A-Za-z]\w*@(\w+\.)*\w+\.com'
s = 'nobby@www.xxx-yyy.com'
m = re.match(patt, s)
print(m)
n = re.search(patt, s)
print(n)