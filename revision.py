print("Welcome to the love calculator!")

name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_string = name1 + name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = (t + r + u + e)

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
love = (l + o + v + e)

love_score = int(str(true) + str(love))
print(love_score)

if love_score < 10 or love_score > 90:
    print(f"your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}")

