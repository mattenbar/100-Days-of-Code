
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


t_count = name1.lower().count('t') + name2.lower().count('t')
r_count = name1.lower().count('r') + name2.lower().count('r')
u_count = name1.lower().count('u') + name2.lower().count('u')
e_count = name1.lower().count('e') + name2.lower().count('e')

l_count = name1.lower().count('l') + name2.lower().count('l')
o_count = name1.lower().count('o') + name2.lower().count('o')
v_count = name1.lower().count('v') + name2.lower().count('v')
e2_count = name1.lower().count('e') + name2.lower().count('e')

true_count = t_count + r_count + u_count + e_count

love_count = l_count + o_count + v_count + e2_count

compatability = str(true_count) + str(love_count)


if compatability < 10 or compatability > 90:
    print(f"Your score is {compatability}, you go together like coke and mentos.")
elif compatability > 39 and compatability < 50:
    print(f"Your score is {compatability}, you are alright together.")
else:
     print(f"Your score is {compatability}.")