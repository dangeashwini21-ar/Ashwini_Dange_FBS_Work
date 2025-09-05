key=int(input("enter a key to remove: "))
dict={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}
if key in dict:
    dict.pop(key)
print(dict)