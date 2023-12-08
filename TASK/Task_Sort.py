


list1= ["Mango","Kiwi","Banana","Apple","Graps"]

print("Before The List: ",list1)


for x in range(0,len(list1)):
    for i in range(x+1,len(list1)):
        if list1[x] >= list1[i]:
            list1[x],list1[i]= list1[i],list1[x]

print("Sorted The List: ",list1)
