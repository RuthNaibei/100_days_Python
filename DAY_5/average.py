# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights split with a comma:\n ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_height = 0

for height in student_heights:
  total_height+=height

number_students=0
for student in student_heights:
  number_students+=1

average=round(total_height/number_students)
print(average)







