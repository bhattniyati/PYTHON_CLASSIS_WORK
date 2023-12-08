
# sort the list without using inbuilt function



list1= [56,80,20,30,24,100,50]

print("Before List: ",list1)

for x in range(0,len(list1)):
    for i in range(x+1,len(list1)):
        if list1[x]>=list1[i]:
            list1[x],list1[i]=list1[i],list1[x]


print("Sorted The List",list1)
