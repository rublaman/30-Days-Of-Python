A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
B.update(A)
print(B)
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
A.update(B)
B.update(A)
print(A)
print(B)
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del A, B
