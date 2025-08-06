str="krishna"
print(len(str)) # This will print the length of the string "krishna" which is 7
print(str.endswith("na")) # This will check if the string ends with "na" and print True
print(str.startswith("kri")) # This will check if the string starts with "kri" and print True
count = str.count("r") 
print(count) # This will count the occurrences of "r" in the string and print 1
print(str.find("s")) # This will find the index of the first occurrence of "s" in the string and print 3
capitalized_string = str.capitalize() 
print(capitalized_string) # This will capitalize the first letter of the string and print "Krishna"
index = str.find("rr") 
print(index) # This will find the index of the first occurrence of "rr" in the string and print -1 (not found)
replaced_string = str.replace("i", "u") 
print(replaced_string) # This will replace all occurrences of "r" with "l" in the string and print "klishna"

#above are very important string methods


print(str.isalpha()) # This will check if all characters in the string are alphabetic and print True
print(str.isalnum()) # This will check if all characters in the string are alphanumeric and print True
print(str.isdigit()) # This will check if all characters in the string are digits and print False
print(str.islower()) # This will check if all characters in the string are lowercase and print True
print(str.isupper()) # This will check if all characters in the string are uppercase and print False
print(str.isnumeric()) # This will check if all characters in the string are numeric and print False
print(str.isprintable()) # This will check if all characters in the string are printable and print True
print(str.swapcase()) # This will swap the case of all characters in the string and print "KRISHNA"
print(str.title()) # This will convert the first character of each word to uppercase and print "Krishna"
print(str.lower()) # This will convert all characters in the string to lowercase and print "krishna"
print(str.upper()) # This will convert all characters in the string to uppercase and print "KRISHNA"
print(str.strip()) # This will remove any leading or trailing whitespace from the string and print "krishna"
print(str.split("a")) # This will split the string at each occurrence of "a" and print ['kr', 'shn', '']
print(str.join(["Hello", "World"])) # This will join the list with the string as a separator and print "HelloKrishnaWorld"
print(str.replace("r", "l")) # This will replace all occurrences of "r" with "l" in the string and print "klishna"
print(str[1:3]) # This will slice the string from index 1 to 2 and print "ri"
print(str[1:]) # This will slice the string from index 1 to the end and print "rishna"
print(str[:3]) # This will slice the string from the start to index 2 and print "kri"
# This code snippet demonstrates various string operations in Python.
# The code snippets provided demonstrate string slicing and various string methods in Python.


# Python String Functions - Quick Cheat Sheet
# 1. Case Conversion
#  - s.upper() → Converts to UPPERCASE
#  - s.lower() → Converts to lowercase
#  - s.title() → Capitalizes first letter of each word
#  - s.capitalize() → Capitalizes first character only
#  - s.swapcase() → Swaps uppercase to lowercase & vice versa
# 2. Whitespace & Character Removal
#  - s.strip() → Removes leading/trailing whitespace
#  - s.lstrip() → Removes left whitespace
#  - s.rstrip() → Removes right whitespace
# 3. Search & Check
#  - s.find(x) → Index of first occurrence (-1 if not found)
#  - s.index(x) → Like find but raises error if not found
#  - s.count(x) → Count occurrences
#  - s.startswith(x) → True if string starts with x
#  - s.endswith(x) → True if string ends with x
#  - 'x' in s → Checks substring existence
# 4. Replace & Split
#  - s.replace(a,b) → Replace all occurrences of a with b
#  - s.split(",") → Splits into list by separator
#  - "-".join(lst) → Joins list into string
# 5. Alignment & Padding
#  - s.center(n,"*") → Centers with padding
#  - s.ljust(n) / s.rjust(n) → Left/right align
#  - s.zfill(n) → Pads with zeros (e.g., "7".zfill(3) → "007")
# 6. Type Check Methods (Return True/False)
#  - s.isalpha(), s.isdigit(), s.isalnum()
#  - s.islower(), s.isupper(), s.isspace(), s.istitle()
# 7. Reverse String (Not a method)
#  - s[::-1] → Reverses string