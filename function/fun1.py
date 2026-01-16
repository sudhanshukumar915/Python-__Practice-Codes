import time


def my_detail():
    print("Hii\n"+"What is your Name ?")
    name=input()
    print(name+" what's your Age ?")
    age=input()
    print("WOW ! "+name+" You looks like your age"+ " you are too good and fit by your health\n"+"NICE!")

my_detail()
print("WHAT YOUR LOVE NAME")
def my_detail2(name):
    print(F"Her name is {name} !\n OOHO")
    print("US k name se lag rha hai?"+ "jase wo !\n"+"SHE LOOKS LIKE THE LIGHT OF MORNING SUN "+" AND HER NAME FEELS LIKE THE NIGHT OF FULL MOON "+"Am i right or wrong?")
    input()
    print("DON'T WORRY BUDDY SHE ALSO LIKE YOU \n"+"WAIT SOME TIME ")


my_detail2(name=input())   #name is parameter #and input k ander jo data dala jaayega wo hoga actual argument

time.sleep(3)
print("GOOD NIGHT BUDDY!")

