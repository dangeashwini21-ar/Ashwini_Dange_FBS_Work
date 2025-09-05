set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
missingSet1=set1.difference(set2)
missingSet2=set2.difference(set1)
print("missing in set 2 as compared to set 1:",missingSet1)

print("missing in set 1 as compared to set2 :",missingSet2)
