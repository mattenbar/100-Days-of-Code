number_range = range(2,101)

total = 0

for number in number_range:
    if number % 2 == 0:
        total += number

print(total)