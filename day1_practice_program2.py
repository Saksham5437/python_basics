#program to calculate total marks, average and percentage of 3 subjects
#Marks of 3 subjects
m1=int(input("Enter marks of subject_1 : "))
m2=int(input("Enter marks of subject_2 : "))
m3=int(input("Enter marks of subject_3 : "))

#calculating total marks
total_marks = m1+m2+m3

#caluclating average

avg = total_marks/3

#calculating percentage
per = (total_marks/300)*100
print("\n")

#Displaying results
print("---Results---\n")
print("Total Marks is : ", total_marks)
print("Average Marks is : ", round(avg, 2))
print(f"Percentage is :  {round(per, 2)}%")