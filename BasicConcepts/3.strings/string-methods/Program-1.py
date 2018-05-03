#WAP to validate a string type and Evaluate
str=input("Enter Some String:-")
if str.isalnum():
    print("This is an Alphanumeric Value:",str)
    if str.isalpha():
        print("This is an Alphabetic Value:",str)
        if str.islower():
            print("This is alphabetic lowercase value:",str)
        else:
            print("This is alphabetic uppercase value:",str)
    else:
        print("It is digit:",str)
elif str.isspace():
    print("It has only space")
else:
    print("Non space special character")

