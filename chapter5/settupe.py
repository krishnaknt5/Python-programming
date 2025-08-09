s1={1,2,3,4,5,6,9,99}
s2={3,4,5,6,65,48,25,22}
print(s1.union(s2))  
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))



# | Method                         | Description                                         |
# | ------------------------------ | --------------------------------------------------- |
# | `add(elem)`                    | Add a unique element to the set                     |
# | `remove(elem)`                 | Remove element; *KeyError* if absent                |
# | `discard(elem)`                | Remove element if present — no error if absent      |
# | `pop()`                        | Remove & return an arbitrary element                |
# | `clear()`                      | Empty the set                                       |
# | `copy()`                       | Create a shallow copy of the set                    |
# | `update(iterable)`             | Add multiple elements from iterable                 |
# | `union(intersections)`         | New set with combined elements                      |
# | `intersection(...)`            | New set with only common elements                   |
# | `difference(...)`              | New set with elements not in the other sets         |
# | `symmetric_difference(...)`    | New set of elements unique to either set            |
# | *(In-place variants of above)* | e.g. `intersection_update()`, `difference_update()` |
# | `isdisjoint(other)`            | Are the sets disjoint (no common members)?          |
# | `issubset(other)`              | Is this a subset of the other?                      |
# | `issuperset(other)`            | Is this a superset of the other?                    |
