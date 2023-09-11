#Write your code below this line 👇
def prime_checker(number):
    start = 2
    while start < number:
        remainder = number % start
        if remainder == 0:
            print("It's not a prime number.")
            return ''
        start+=1
    print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
