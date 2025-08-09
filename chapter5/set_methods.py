s={1,2,99}
s.add(55,66) # this will add 55 and 66 to the set
print(s)  

























# | **Method / Operator**                                 | **Description**                                   | **Modifies Set?**                             | **Raises Error?**           |      |
# | ----------------------------------------------------- | ------------------------------------------------- | --------------------------------------------- | --------------------------- | ---- |
# | `add(elem)`                                           | Adds `elem` to the set                            | ✅ Yes                                         | ❌ No                        |      |
# | `remove(elem)`                                        | Removes `elem`; raises error if not present       | ✅ Yes                                         | ✅ Yes (`KeyError`)          |      |
# | `discard(elem)`                                       | Removes `elem` if present; does nothing if not    | ✅ Yes                                         | ❌ No                        |      |
# | `pop()`                                               | Removes and returns an arbitrary element          | ✅ Yes                                         | ✅ Yes (`KeyError` if empty) |      |
# | `clear()`                                             | Removes all elements from the set                 | ✅ Yes                                         | ❌ No                        |      |
# | `copy()`                                              | Returns a shallow copy of the set                 | ❌ No                                          | ❌ No                        |      |
# | `union(*others)` / \`set1                             | set2\`                                            | Returns a new set with elements from all sets | ❌ No                        | ❌ No |
# | `intersection(*others)` / `set1 & set2`               | Returns a new set with common elements            | ❌ No                                          | ❌ No                        |      |
# | `difference(*others)` / `set1 - set2`                 | Returns a set with elements only in the first set | ❌ No                                          | ❌ No                        |      |
# | `symmetric_difference(other)` / `set1 ^ set2`         | Returns elements in either set, but not both      | ❌ No                                          | ❌ No                        |      |
# | `update(*others)` / \`set1                            | = set2\`                                          | Adds all elements from other sets (union)     | ✅ Yes                       | ❌ No |
# | `intersection_update(*others)` / `set1 &= set2`       | Keeps only common elements (intersection)         | ✅ Yes                                         | ❌ No                        |      |
# | `difference_update(*others)` / `set1 -= set2`         | Removes all elements found in others              | ✅ Yes                                         | ❌ No                        |      |
# | `symmetric_difference_update(other)` / `set1 ^= set2` | Keeps only elements in either set, but not both   | ✅ Yes                                         | ❌ No                        |      |
# | `issubset(other)` / `set1 <= set2`                    | Returns `True` if `set1` is a subset of `other`   | ❌ No                                          | ❌ No                        |      |
# | `issuperset(other)` / `set1 >= set2`                  | Returns `True` if `set1` is a superset of `other` | ❌ No                                          | ❌ No                        |      |
# | `isdisjoint(other)`                                   | Returns `True` if sets have no elements in common | ❌ No                                          | ❌ No                        |      |
