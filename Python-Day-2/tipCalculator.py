bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
amount_of_people = int(input("How many people to split the bill? "))

split_total = bill / amount_of_people
amount_to_pay = round(split_total * (tip/100 + 1), 3)

print(f"Each person should pay: ${amount_to_pay:.2f}")
