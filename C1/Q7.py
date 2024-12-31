# Determine grade earned by student based on KTU scale

percent = 95

grade = ""
if percent >= 90:
    grade = "S"
elif 85 <= percent < 90:
    grade = "A+"
elif 80 <= percent < 85:
    grade = "A"
elif 75 <= percent < 80:
    grade = "B+"
elif 70 <= percent < 75:
    grade = "B"
elif 65 <= percent < 70:
    grade = "C"
elif 60 <= percent < 65:
    grade = "D"
elif 55 <= percent < 60:
    grade = "P"
else:
    grade = "F"

print(grade)