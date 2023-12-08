

l1= [20,10,20,30,66,77,80,10]


unique_values=[]


for x in l1:
    if x not in unique_values:
        unique_values.append(x)


print("Original List: ",l1)
print("List with Duplicate values Removed: ",unique_values)


