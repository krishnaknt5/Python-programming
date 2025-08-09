#this program is about tuples in Python

t = (3, 1, 2, 1, 5)
print(type(t))  # Output: <class 'tuple'>
print(t.count(1)) # Count occurrences of 1  
print(t.index(5))  # Find index of first occurrence of 5 
print(len(t)) # Length of the tuple      
print(min(t), max(t)) # Minimum and maximum values in the tuple
print(sorted(t)) # Sorted version of the tuple (returns a list)        
print(tuple([7, 8, 9]))    # Convert list to tuple means build a new tuple from iterable with these valuestuple()
print(t + (6, 7))         # Concatenate tuples means adding these elements iinto the tuple
print(t * 2) # Replicate the tuple  means giving the output 2 times like a*2=2a                   


#billow is functions table for tuples in Python


# | Operation         | Method/Function            | Description                      |
# | ----------------- | -------------------------- | -------------------------------- |
# | Count occurrences | `t.count(x)`               | Return how many times `x` occurs |
# | Find item index   | `t.index(x[, start, end])` | Return first position of `x`     |
# | Length            | `len(t)`                   | Return number of elements        |
# | Min / Max         | `min(t)`, `max(t)`         | Smallest / largest item          |
# | Sort              | `sorted(t)`                | Returns **list** sorted version  |
# | Convert           | `tuple(iterable)`          | Build tuple from iterable        |
# | Concatenate       | `t1 + t2`                  | Join two tuples                  |
# | Replicate         | `t * n`                    | Repeat tuple `n` times           |
# | Delete tuple      | `del t`                    | Remove entire tuple object       |
