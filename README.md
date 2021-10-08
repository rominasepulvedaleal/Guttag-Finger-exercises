# Guttag-Finger-exercises
#These are my answer to finger exercises  for Introduction to Computing and Programming using Python (Guttag, 2013)
Finger exercise 2.1: Write a program that examines three variables— x , y , and z — #and prints the largest odd number among them. If none of them are odd, it #should print a message to that effect.

x=int(input('Enter x: '))
y=int(input('Enter y: '))
z=int(input('Enter z: '))

if x>y>z and x%2==1:
    print(str(x),' is the largest odd number')
elif y>z and y%2==1:
    print(str(y),' is the largest odd number')
elif z%2==1:
    print(str(z),' is the largest odd number')
else:
    print('none of them is odd')
