#accept marks of six students and display them in sorted mannner

marks = []
f1 = int(input("Enter marks 1: "))
marks.append(f1)
f2 = int(input("Enter marks 2: "))
marks.append(f2)
f3 = int(input("Enter marks 3: "))
marks.append(f3)
f4 = int(input("Enter marks 4: "))
marks.append(f4)
f5 = int(input("Enter marks 5: "))
marks.append(f5)

marks.sort()
print(marks)

t = type(f1)
print(t)