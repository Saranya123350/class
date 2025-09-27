# set: {}, no duplicate values, unordered, unindexing, fastest 
"""
city={"chennai","hyderabad","Banglore"} 
city.add("Puri")
city.pop()
city.remove("chennai")
city.discard("vrindavan")
city.update("chennai","arunachalam")
print(city)
"""
# set theory: union, intersection, difference, subset, superset, isdisjoint (symmetric_difference=(a-b)union(b-a)), union_update= change things in first set
#intersection= ^, union= | 
"""
surv_1={'Emp_(1)','Emp_(2)','Emp_(3)','Emp_(4)','Emp_(5)','Emp_(6)'}
surv_2={'Emp_(9)','Emp_(8)','Emp_(3)','Emp_(4)','Emp_(5)','Emp_(10)'}
print(surv_1.intersection(surv_2))
print(surv_1.union(surv_2))
print(surv_1.difference(surv_2))
print(surv_1.symmetric_difference(surv_2))
print(surv_1.isdisjoint(surv_2))
print(surv_1.issubset(surv_2))
details=list({'Emp_(1)','Emp_(2)','Emp_(3)','Emp_(4)','Emp_(5)','Emp_(6)'})
print(details)
"""
# Tuple: (), no changes can be made in tuple, indexing, ordered
"""
age=3
s=(3,5,1,2,1,3,{3,4,5,6})
a=s[6].add("8")
print(s.index(5))
print(s.count(3))
print(s)
print(id(age))
print(id(s[0]))
"""