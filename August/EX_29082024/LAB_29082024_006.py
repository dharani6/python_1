#tuple
tuple1 = (1,2,3,4,4,4,4)
print(len(tuple1),tuple1)

print(tuple1.count(4))

tup_list = list(tuple1)
tup_list.extend([4,4,4,3,3,2,2,2])
rdh = tuple(tup_list)

print(rdh,tuple(tup_list))
print(sorted(rdh), rdh)

a,b,c = (10,11,12)
print(a,b,c)
aa,bb,cc =[11,22,33]
print(aa,"\n", bb,'\n', cc)
rdh = rdh +(2,3,44)
print(rdh)