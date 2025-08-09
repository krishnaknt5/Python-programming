# Can we have a set with 18 (int) and '18' (str) as a value in it? (Yes, we can)
s = ()
s.add(18)
s.add('18')
print(s)


#or

set = {18, '18'}

print(set)
print(type(18))
print(type('18'))
print(len(set))