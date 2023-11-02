
percentage = int(input("Enter the percentage: "))

if 90 <= percentage <= 100:
    grade = 'A'
elif 80 <= percentage < 90:
    grade = 'B'
elif 70 <= percentage < 80:
    grade = 'C'
elif 60 <= percentage < 70:
    grade = 'D'
elif 0 <= percentage < 60:
    grade = 'F'
else:
    grade = 'Invalid percentage'

print(f"Percentage {percentage}% corresponds to Grade {grade}")
