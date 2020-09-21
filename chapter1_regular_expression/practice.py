import re
# s = 'M. ws'
# patten = '(Mr)?s?\.'
# result = re.findall(patten, s)
# print(result)


#
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))
