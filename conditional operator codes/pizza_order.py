print("Welcome to the pizza world")
size=input("Which Size of Pizza do You Want \n"+"S,M or L ")
perpeponi=input("Do You want to perpeponi on your Pizza ? YES or NO \n")
extra_chess=input("Do you want to extra chess? YES or NO \n")

print("Price of pizza \n")

bill=0
if size=='S':
    bill+=50
elif size=='M':
     bill+=70
elif size=='L':
     bill+=100
else:
    print("your type is wrong ")
print("price of perpeponi on the pizza ")
if perpeponi == "YES":
    if size=="S":
        bill+=2
    else:
        bill+=3
else:
 print("Thanks for shearing Information \n")
 print("Do YOU want to extra chess ? \n")
if extra_chess=="YES":
    bill+=3
else:
    print("Thanks for shearing Information ?\n")



