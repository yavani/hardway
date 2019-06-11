from collections import OrderedDict
print("this is dict")

d={ }
d['a']=1
d['b']=2
d['c']=3
d['d']=4

for key,values in d.items():
	print(key,values)

print("this is order dict")

od= OrderedDict()
od['a']=2
od['b']=1
od['c']=4
od['d']=7

for k,v in od.items():
	print(k,v)

dict={"banana","papaya","apple","chiku"}

for fruits in sorted(set(dict)):
	print(fruits)

for i in reversed(range(1,10,2)):
	print(i)

dict1=OrderedDict()
dict1["name"]=1
dict1['religon']=2
dict1['favourite color']=3
dict2=OrderedDict()
dict2["Ashwini"]=1
dict2["hindu"]=2
dict2["blue"]=3


for d1,d2 in zip(dict1,dict2):
	print("what is your {0} ? it is {1} .".format(d1,d2))
