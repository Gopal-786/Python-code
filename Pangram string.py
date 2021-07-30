str = input("Enter the String you want to check :")

str = str.lower()

alpha = "abcdefghijklmnopqrstuvwxyz"

check = True

for i in alpha :

    if i in str :

        check = True

    else :

        check = False

if check == True :

    print("String is PANGRAM")

else :

    print("String is not PANGRAM")
