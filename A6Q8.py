str1=input("Enter the integers separated by a space")
set1=[*set(str1.split(" "))]
for i in set1:
    print(i)
    i=int(i)
    print(i)
print(set1)