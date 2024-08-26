"""
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)
# Creating a Set with a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)
# Creating a Set with the use of a tuple
t = ("Geeks", "for", "Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print("\nSet with the use of Dictionary: ")
print(set(d))
"""

# Creating a Set
set1 = set([15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)
# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)
