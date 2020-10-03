### Author: Kubam Ivo
### Date: 10/1/2020

x1 = int(input("Enter the x1 coordinate: "))
y1 = int(input("Enter the y1 coordinate: "))
x2 = int(input("Enter the x2 coordinate: "))
y2 = int(input("Enter the y2 coordinate: "))
distance = (((x1-x2)**2) + ((y1-y2)**2))**0.5
print("The euclidian distance between those points is :", distance)