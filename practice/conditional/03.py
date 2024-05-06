# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score:
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter the score"))

if(score > 100):
    print("enter the valid score")
elif(score >=90 and score <= 100):
    print("Grade A")
elif(score >=80 and score <= 89):
    print("Grade B")
elif(score >=70 and score <= 79):
    print("Grade C")
elif(score >=60 and score <= 69):
    print("Grade D")
elif(score < 60):
    print("Grade E")