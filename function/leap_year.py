def is_leap_year(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False


year=int(input("Enter The Year :"))
variable_year=is_leap_year
if variable_year:
    print(f"{year} is leap year")
else:
    print(f"{year} is leap year")
