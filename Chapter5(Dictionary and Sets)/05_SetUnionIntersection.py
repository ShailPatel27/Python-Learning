s1 = {1,2,3,4}
s2 = {2,3,4,5}
s3 = {2,3}

print("union:",  s1.union(s2) )
print("union:",  s1 | s2 )

print("intersection:",  s1.intersection(s2) )
print("intersection:",  s1 & s2 )

print("difference:",  s1.difference(s2) )
print("difference:",  s1 - s2 )

print("symmetric difference:",  s1.symmetric_difference(s2) )
print("symmetric difference:",  s1 ^ s2 )

print("is subset?",  s3.issubset(s2) )
print("is superset?",  s1.issuperset(s2) )