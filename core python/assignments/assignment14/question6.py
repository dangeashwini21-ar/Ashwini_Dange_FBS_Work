li=[1,2,3,4,6,7,8,5,1]
set=set(li)
li=sorted(set)
p1=li[-1]*li[-2]
p2=li[0]*li[1]
if p1>p2:
    print("pair:",li[-1],li[-2])
    print("max product:",p1)
else:
    print("pair:",li[0],li[1])
    print("max product:",p2)

