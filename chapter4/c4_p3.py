# 3. Check that a tuple type cannot be changed in python.
t = (1, 2, "kkd")
try:
    t[3] = 10
except TypeError as e:
    print("Error:", e)
# Tuples are immutable

# or



t = (1, 2, "kkd")
t[3] = 10
#op:= Tuples are immutable
