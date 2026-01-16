import random
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','^','&','*','(',')','<','>',',','.',';',':','?','/','{','}','[',']','|','+','=','-','_']
alphabeta=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("WELCOME TO PASSWORD GENERATOR\n")
enter_number=int(input("HOW MANY LETTER DO YOU WANT TO GENERATE YOUR PASSWARD :\n"))
enter_symbol=int(input("HOW MANY SYMBOLS DO YOU WANT TO GENERATE YOUR PASSWARD:\n"))
enter_alphabets=int(input("HOW MANY ALPHABETS DO YOU WANT TO  GENERATE YOUR PASSWARD:\n"))

#
password= ""
for char in range(1,enter_symbol+1):
    password+=random.choice(symbol)
for char in range(1, enter_alphabets + 1):
    password += random.choice(alphabeta)
for char in range(1, enter_number + 1):
        password += random.choice(number)

print("YOUR PASSWARD IS :"+password)


