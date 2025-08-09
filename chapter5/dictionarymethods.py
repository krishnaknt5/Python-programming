#a={} is an empty dictionary


marks={"john": 85, 
       "Alice": 90, 
       "Bob": 78,}




#updatte methods
# marks.update({"john":44, "rakhi":55}) #updating the value of key "john" by using update operation
# print(marks)

# if i add a new key "rakhi" with value 55, it will be added to the dictionary


#get method
print(marks.get("raju")) # this will return None as "raju" is not a key in the dictionary

print(marks.get("john")) # this will return 85 if i didnt use update method if i use it will give 44 as "john" is a key in the dictionary
print(marks["john2"]) # this will return KeyError as "john2" is not a key in the dictionary
#the above 2 lines are same but the first one will not give error if the key is not present in the 








# | Method                            | Description                                                                                   |
# | --------------------------------- | --------------------------------------------------------------------------------------------- |
# | `dict.clear()`                    | Removes all items from the dictionary.                                                        |
# | `dict.copy()`                     | Returns a shallow copy of the dictionary.                                                     |
# | `dict.fromkeys(seq[, value])`     | Creates a new dictionary with keys from `seq` and values set to `value` (defaults to `None`). |
# | `dict.get(key[, default])`        | Returns the value for `key` if key is in the dictionary, else returns `default`.              |
# | `dict.items()`                    | Returns a view object of `(key, value)` pairs.                                                |
# | `dict.keys()`                     | Returns a view object of all keys.                                                            |
# | `dict.pop(key[, default])`        | Removes the specified key and returns the value. If key is not found, returns `default`.      |
# | `dict.popitem()`                  | Removes and returns the last `(key, value)` pair inserted.                                    |
# | `dict.setdefault(key[, default])` | Returns the value of `key`. If not present, inserts `key` with a value of `default`.          |
# | `dict.update([other])`            | Updates the dictionary with key/value pairs from `other`, overwriting existing keys.          |
# | `dict.values()`                   | Returns a view object of all values.                                                          |

#example of dictionary methods

person = {'name': 'Alice', 'age': 25}

# get()
print(person.get('name'))         # Alice
print(person.get('city', 'N/A'))  # N/A

# setdefault()
person.setdefault('city', 'New York')
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# update()
person.update({'age': 26, 'email': 'alice@example.com'})
print(person)

# pop()
age = person.pop('age')
print(age)     # 26
print(person)  # 'age' is removed

# keys(), values(), items()
print(person.keys())    # dict_keys(['name', 'city', 'email'])
print(person.values())  # dict_values(['Alice', 'New York', 'alice@example.com'])
print(person.items())   # dict_items([('name', 'Alice'), ('city', 'New York'), ('email', 'alice@example.com')])
