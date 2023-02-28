for number in range(1, 101):
  #first bug is change or for and
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  #change if for elif
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    #Eliminate the []
    #print([number])
    print(number)
    