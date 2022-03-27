import math
radius = float(input("enter the radius of the circle : "))
area = math.pi * radius * radius
print("area of the circle is : {0}".format(area))

filename = input("write the filename")
file_extns = filename.split(".")
print ("the extention is" + repr(file_extns[-1]))
