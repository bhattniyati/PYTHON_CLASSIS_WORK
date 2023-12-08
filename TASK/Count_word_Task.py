'''
# Split The String And Count Word

name= input("Enter a String: ")

print(name.split(' '))
print(len(name))

char= input("Enter A Character: ")
'''

# Check The Char is in the String Nd Print Msg Exit And Does'nt Exit And Count The Frequency

string= input("Enter a String: ")
char= input("Enter A Character: ")

count=0

for char in string: 
    if char==char:
        count+=1
    print("count",count)

if char in string:
    print("Exit: The Character is in the string..")
else:
    print("Does not Exit: The Character is not in the string")















