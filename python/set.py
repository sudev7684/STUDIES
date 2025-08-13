# s={1,2,3,4}
# s.add(5)
# print(s)
# s.update({6, 7, 8})
# print(s)
# s.pop()
# print(s)
# s.remove(3)
# print(s)
# s.discard(3)
# print(s)


# s={1,2,2,3,4}
# s1={1,2,3,4,5,6,7}
# print(s1.difference(s))
# print(s1.intersection(s))
# print(s1.isdisjoint(s))
# print(s1.issubset(s))
# print(s1.issuperset(s))
# print(s1.symmetric_difference(s))
# print(s1.union(s))
# s.copy()
# print(s)

s={1,2,3,4,8}
s1={1,2,3,4,5,6,7}
print(s)
s.difference_update(s1)
s.intersection_update(s1)  
s.symmetric_difference_update(s1)
print(s) 
     


