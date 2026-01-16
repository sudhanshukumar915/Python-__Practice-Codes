Bucket={"color":"Red,Green,Yellow,White,Black",
        "fruit":"Banana,gauva,Apple,Coconut,pineapple,Kiwi",
        "Name":"rishu,afroz,sangam,amit,sudhanshu"}      #creating dictianory

print(Bucket["fruit"],"\n"+Bucket["Name"])               #using multiple key to display disctionay elemants
Bucket["food"]={"chiecken,muttan,egg,omlet,penut-Butter and bread"}         #adding some new element in dictionary
print(Bucket)

#Using loop to display all key with elements of Bucket
for item in Bucket:
    print(item)
    print(Bucket[item])
