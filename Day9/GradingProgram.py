student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  scores = student_scores[key]
  grade = ""
  if scores >= 91:
    grade = "Outstanding"
  elif scores >= 81:
    grade = "Exceeds Expectations"
  elif scores >= 71:
    grade = "Acceptable"
  elif scores <= 70:
    grade = "Fail"  

  student_grades[key] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
