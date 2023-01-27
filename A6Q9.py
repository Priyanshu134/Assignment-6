str1=input("Enter the string of parantheses")
for i in ["(("]:
    if i in str1:
        print("Invalid")
    else:
        print("Valid")