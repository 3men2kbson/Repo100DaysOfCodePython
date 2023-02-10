#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
peoples = input("How many people to split the bill? ")

person_to_pay = round((float(total_bill) / int(peoples)) * (1 + int(percentage_tip) / 100), 2)

person_to_pay = "{:.2f}".format(person_to_pay)

message_result = f"Each person should pay: ${ person_to_pay }" 
print(message_result)