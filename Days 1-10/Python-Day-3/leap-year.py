year = int(input("Which year do you want to check? "))

def check_if_leap_year(year): 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

leap = check_if_leap_year(year)

if leap:
    print("Leap year.")
else:
    print("Not leap year.")