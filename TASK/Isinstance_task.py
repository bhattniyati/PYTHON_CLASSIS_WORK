
l1= [12,3.434,45,"Hello",74,34.54,"Happy",'Alpha']

integers=[]
floats= []
strings= []


for element in l1:
    if isinstance(element,int):
        integers.append(element)

    elif isinstance(element,float):
        floats.append(element)

    elif isinstance(element,str):
        strings.append(element)

    else:
        print("unknwon type")


print("Integers: ", integers)
print("floats: ", floats)
print("strings: ", strings)

