
def format_name(first_name,last_name):
    #print(first_name.title())
    #print(last_name.title())
    variable1=first_name.title()
    variable2=last_name.title()
    return f"{variable1},{variable2}"

variable3=format_name(first_name=input("ENTER YOUR FIRST NAME:\n"),last_name=input("ENTER YOUR LAST NAME:\n"))
print(variable3)