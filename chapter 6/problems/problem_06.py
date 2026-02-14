'''Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
'''

marks = int(input("enter marks of student: "))

if(90<marks<=100):
    print("grade Ex")
elif(80<marks<=90):
    print("grade A")
elif(70<marks<=80):
    print("grade B")
elif(60<marks<=70):
    print("grade C")
elif(50<marks<=60):
    print("grade D")
elif(marks<50):
    print("grade F")