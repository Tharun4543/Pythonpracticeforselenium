set1={10,"tharun","tharun",20}
# print(s)
# print(len(s))
# for i in s:
#     print(i)
# s.add("selva")
# print(s)
# s.update(["Sitha","ram"])
# print(s)
# s.remove(20)
# print(s)
# s.remove("sitha")
# s.discard("tharun")
# print(s)
# s.discard(30)
set2=set1.copy()
# print(set2)
print(set1)
#print(set2)
#print(set1.union(set2))
set2={"sitha","tharun"}
#print(set1.symmetric_difference(set2))
print(set1.difference(set2))
#print(set1.difference_update())
# print(set1.intersection(set2))
# print(set1.issubset(set2))
print(set1.clear())
print(set1)
del set1
print(set1)
