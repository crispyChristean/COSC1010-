#
# Christian
# 9/14/2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
lengthA = 0
widthB = 0

lengthB = 0
widthB = 0

areaA = 0 
areaB = 0
# Get length A
# Get width A
# Get length B
# Get width B
lengthA = float(input("what is the length of the first rectangle? "))
widthA = float(input("what is the width of the first rectangle? "))

lengthB = float(input("what is the length of the second rectangle? "))
widthB = float(input("what is the width of the second rectangle? "))

# Calculate area A
# Calculate area B
areaA = lengthA * widthA
areaB = lengthB * widthB

# Print area comparison using if-elif-else statements
if areaA == areaB:
    print("Both the first and second rectangle have the same area!!!!!!")

elif areaA > areaB:
    print("The first triangle's area is greater than the second triangles area!!")

elif areaA < areaB:
    print("The second triangle's area is greater than the first triangle's area!!!")
else:
    print("What???")


    # I did the hot dog one first so this one was surprisingly much easier and direct