from math import pi
r = float(input("write the radius of the circle"))
print("area of the circle is " + str(r)+"is:"+str(pi*r**2))


filename = input("write the filename")
file_extns = filename.split(".")
print ("the extention is" + repr(file_extns[-1]))
