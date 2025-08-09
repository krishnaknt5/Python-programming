l1=[10,5,9,4,66,38,5]
l2=[10,5,9,4,66,38,5]
l3=[10,5,9,4,66,38,5]
l4=[10,5,9,4,66,38,5]
l5=[10,5,9,4,66,38,5]
l6=[10,5,9,4,66,38,5]
l7=[10,5,9,4,66,38,5]
l8=[10,5,9,4,66,38,5]
l1.append(25) # Adding an element at the end of the list
l2.sort()# Sorting the list (ascending order)
l3.reverse()# Reversing the list ((ab=ba))
l4.insert(2, 14)# Inserting an element at index 2(2 is a specified position)
l5.pop(3)# Removing the element at index 3 (3 is a specified position)
l6.remove(5)# Removing the first occurrence of 5(5 is a specified value)
l7.extend([12, 15, 18])# Extending the list with another list(adding element at the end and making a new list)
l8.clear()# Clearing the complete list
print(l1, l2, l3, l4, l5, l6, l7, l8)# Outputting the modified lists  



# in the above program if i take only one list and perform all the operations on it, it will give the output of the last operation ehich is clear(). 




# l1=[10,5,9,4,66,38,5]   wrong
# l1.append(25)
# l1.sort()
# l1.reverse()            wrong
# l1.insert(2, 14)
# l1.pop(3)               wrong
# l1.remove(5)
# l1.extend([12, 15, 18]) wrong
# l1.clear()
# print(l1)  this is wrong  




# i can use either first method or this billow method to perform the operations on a single list
l1 = [10, 5, 9, 4, 66, 38, 5]
print(f"Initial list: {l1}")

l1.append(25)
print(f"After append(25): {l1}")

l1.sort()
print(f"After sort(): {l1}")

l1.reverse()
print(f"After reverse(): {l1}")

l1.insert(2, 14)
print(f"After insert(2, 14): {l1}")

popped_element = l1.pop(3)
print(f"After pop(3) (removed {popped_element}): {l1}")

l1.remove(5)
print(f"After remove(5): {l1}")

l1.extend([12, 15, 18])
print(f"After extend([12, 15, 18]): {l1}")

l1.clear()
print(f"After clear(): {l1}")





# | Method                             | Description                                                                                                       |
# | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
# | `append(x)`                        | Adds an item `x` to the **end** of the list ([Python documentation][1])                                           |
# | `extend(iterable)`                 | Adds all elements from `iterable` to the end ([Python documentation][1], [GeeksforGeeks][2])                      |
# | `insert(i, x)`                     | Inserts item `x` before index `i` ([Python documentation][1], [GeeksforGeeks][2])                                 |
# | `remove(x)`                        | Removes the **first** occurrence of value `x` ([Python documentation][1], [GeeksforGeeks][2])                     |
# | `pop([i])`                         | Removes and *returns* item at index `i` (default: last) ([Python documentation][1], [GeeksforGeeks][2])           |
# | `clear()`                          | Removes *all* items from the list ([Python documentation][1], [GeeksforGeeks][2])                                 |
# | `index(x[, start[, end]])`         | Returns the index of the first `x` between `start` and `end` ([Python documentation][1], [GeeksforGeeks][2])      |
# | `count(x)`                         | Returns the **number** of times `x` appears ([Python documentation][1], [GeeksforGeeks][2])                       |
# | `sort(*, key=None, reverse=False)` | Sorts the list *in-place* (customizable with `key` and `reverse`) ([Python documentation][1], [GeeksforGeeks][2]) |
# | `reverse()`                        | Reverses the list *in-place* ([Python documentation][1], [GeeksforGeeks][2])                                      |
# | `copy()`                           | Returns a **shallow copy** of the list ([Python documentation][1], [GeeksforGeeks][2])                            |

