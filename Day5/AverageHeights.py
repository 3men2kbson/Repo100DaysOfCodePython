# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

count = 0
total_heights = 0
average_heights = 0

for height in student_heights:
  total_heights += height
  count = count + 1

average_heights = total_heights / count

print(round(average_heights))
