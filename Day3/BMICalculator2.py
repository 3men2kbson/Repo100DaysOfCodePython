height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / float(height) ** 2
bmi = round(bmi, 1)

#print(int(bmi))
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are\033[1m underweight\033[0m.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a\033[1m normal weight\033[0m.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are\033[1m slightly overweight\033[0m.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are\033[1m obese\033[0m.")
else:
  print(f"Your BMI is {bmi}, you are\033[1m clinically obese\033[0m.")