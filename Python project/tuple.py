# tuple in python 
tup=(1,2,34,4,5,56,7,77,8,5,4.535,"eprferfe","eokroekfo") # any type of data store in tuple float,string, integer type any type of data can be store
print(tup)
print(type(tup))
print(len(tup))
print(tup[4])

print(tup[0])
# create loop in tuples 
sum=0
for val in tup:
    sum +=1
print(f"sum of val is {sum}")

def tupl():
    tup=(1,2,3,4,5,6,7,8,8,9,9,9,9,9,99,99999,9,99,99,99,9,9,9,9,9,99,9,9,9)
    print(tup)
    print(tup.count(99999))
    
tupl()
    
