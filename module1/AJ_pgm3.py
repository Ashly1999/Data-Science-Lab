
def checkTriangle(x, y, z):

 if x == y == z:
  print("Equilateral Triangle")


 elif (x == y or y == z or z == x):
  print("Isosceles Triangle")


 else:
    print("Scalene Triangle")



x = int(input("Enter the first side"))
y = int(input("Enter the second side"))
z = int(input("enter the third side"))


checkTriangle(x, y, z)