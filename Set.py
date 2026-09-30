# set - not order based , it stores different types of data
# It does not store duplicate elements

# define a set: use {}

s1 = {100, "Tom", "12.33", True}
s2 = {1, 2, 1, 2, 1, 1, 3, 2}
print(s2)
print(s1)

# set() function:

s3 = set([100, 200, 300, 400, 100])
print(s3)

s4 = set("python")
print(s4)

s5 = set((10, 20, 30, 40, 20, 30))
print(s5)

# while creating a set object, you can store only Numbers, Strings , tuples
# list and dictionary objects are not allowed

set1 = {10, "Tom", (10, 20, 30)}
print(set1)

# set2 = {[10,20,30], [40,50,60], [70,80,90]}
# print(set2) # This will give TypeError: unhashable type: 'list'

# set operations:
# union:
p1 = {1, 2, 3, 4, 5}
p2 = {4, 5, 6, 7, 8}

print(p1.union(p2))

# Intersection:
print(p1.intersection(p2))

# difference of sets:
p3 = p1.difference(p2)
print(p3)  # elements in p1 but not in p2

# symmetric difference of sets:
p4 = p1.symmetric_difference(p2)
print(p4)  # elements in p1 or p2 but not in both

# subset:
p5 = {1, 2, 3}
p6 = {1, 2, 3, 4, 5}
print(p5.issubset(p6))  # True if all elements of p5 are in p6

# superset
p7 = {1, 2, 3, 4, 5}
p8 = {1, 2, 3}
print(p7.issuperset(p8))  # True if all elements of p8 are in p7

# In Built methods
# Add elements to a set
s1 = {"Java", "Python", "C++"}
s1.add("Perl")
print(s1)

# Update elements to a set
s1.update(["C", "Ruby"])
print(s1)

# clear:
s1.clear()
print(s1)

# copy
lang = {"Python", "Java", "C++"}
lang1 = lang.copy()
print(lang1)

# discard:
lang = {"Python", "Java", "C++"}
lang.discard("Java")
print(lang)

# remove:
student = {"Keshav", "Tom", "Steve"}
student.remove("Tom")
print(student)
