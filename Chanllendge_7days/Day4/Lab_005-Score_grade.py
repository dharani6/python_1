# Write a program that calculates and displays the letter grade for a
# given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# If, elif, else

Score = int(input("Enter the Score you got!!!\n"))


def Grade_system(Score):
    if 100 > Score >= 90:# 90>= Score <=100
        print("your grade is A")
    elif 89 >= Score >= 80:
        print("your grade is B")
    elif 79 >= Score >= 70:
        print("your grade is C")
    elif Score <= 69 and Score >= 60:
        print("your grade is D")
    elif Score <= 59 and Score >= 0:
        print("your grade is F")
    else:
        print(f"input is invalid {Score}")


Grade_system(Score)

#liis = [30, 40, 50, 60]
'''print(list(map,Grade_system(liis)))'''

#for i in liis:
 #   Grade_system(i)
