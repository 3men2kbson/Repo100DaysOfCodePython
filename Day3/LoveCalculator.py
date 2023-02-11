# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

couple = name1.lower() + name2.lower()

true_total = couple.count("t")
true_total += couple.count("r")
true_total += couple.count("u")
true_total += couple.count("e")

love_total = couple.count("l")
love_total += couple.count("o")
love_total += couple.count("v")
love_total += couple.count("e")

love_score = str(true_total) + str(love_total)
love_score = int(love_score)

if love_score <= 10 or love_score >= 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")