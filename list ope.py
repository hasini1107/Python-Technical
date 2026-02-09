lis=[1,9,2,6]
print(lis)
#adding append(),extend(),insert()
lis.append(10)
print(lis)
lis2=[7,3,7,2]
lis.extend(lis2)
print(lis)
lis.insert(3,62)
print(lis)
#modifications
lis[3]=6
print(lis)
lis[4:7]=[16,1,17]
print(lis)
# print n access
lis.reverse()
print(lis)
#delete pop(),remove(),del,clear()
lis.pop()
print(lis)
lis.remove(2)
print(lis)
del lis[3]
print(lis)
del lis[1:4]
print(lis)
lis.clear()
print(lis)
del lis
print(lis)