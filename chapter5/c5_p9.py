# Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}

# '''In Python, you cannot have a set that contains a list (like [1, 2])
# as an element, because lists are mutable and therefore unhashable, 
# and only hashable (immutable) types like integers, strings, tuples 
# or frozensets can be in a set'''