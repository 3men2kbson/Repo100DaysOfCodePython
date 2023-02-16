even_sum = 0

for number in range(1, 101):
  evenodd = number % 2
  
  if evenodd == 0:
    even_sum += number

print(f"The sum of even is : {even_sum}")
