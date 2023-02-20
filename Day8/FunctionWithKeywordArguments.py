# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

##Function simple
#def greet():
#  print("Hello")
#  print("Hi")
#  print("What's up?")
#
#greet()

##Function that allows for input
#def greet_with_name(name):
#  print(f"Hello {name}")
#  print(f"Hi {name}")
#  print(f"What's up {name}?")
#
#greet_with_name("Juan")

##Functions with more than 1 input
#def greet_with(name, location):
#  print(f"Hello {name}")
#  print(f"What is it like in {location}")
#
#greet_with("Juan de los Palotes", "Tangamandapio")
##vs
#greet_with("Tangamandapio", "Juan de los Palotes")

#Functions with keyword arguments
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with(name="Juan de los Palotes", location="Tangamandapio")
#vs
greet_with(location="Tangamandapio", name="Juan de los Palotes")
