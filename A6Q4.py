def check_panagram():
    str1=input("Enter the string you want to check for panagram\n")

    str2="abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    is_panagram=True
    for i in range(1,27):
        if ((str2[i-1] not in str1) and (str2[i+25] not in str1)):
            is_panagram=False

    if is_panagram==True:
        print("The entered string is a panagram\n")
    else:
        print("The entered string is not a panagram\n")

while True:
    check_panagram()
