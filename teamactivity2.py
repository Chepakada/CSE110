import math
print('Please enter the units in centimeter')


squareside= float(input('Please enter length of the side of square. '))
print(f'The area of the square is {(squareside)**2} cm^2.')
print(f'The area of the square is {(squareside/100)**2:.3f} m^2.')
print(f'The volume of the  {squareside ** 3:.3f} cm^3.')
print(f'The volume of the  {(squareside/100) ** 3:.3f} m^3.')

rectangleside1=float(input('Please input length of the rectangle. '))
rectangleheight=float(input('Please input the height of the rectange. '))
rectangleside2=float(input('Please input breadth of the rectangle. '))
print(f'The area of the rectangle is {rectangleside1 * rectangleside2:.3f} cm^2')
print(f'The area of the rectangle is {rectangleside1/100 * rectangleside2/100:.3f} m^2')
print(f'The volume of the rectangle is {rectangleside1*rectangleheight*rectangleside2:.3f} cm^3')
print(f'The volume of the rectangle is {rectangleside1/100 * rectangleheight/100 * rectangleside2/100:.3f} m^3')

circleradius=float(input('Please input the radius of circle. '))
print(f'The area of circle is {math.pi * circleradius**2:.2f} cm^2.')
print(f'The area of circle is {(math.pi * circleradius/100)**2:.2f}.')
print(f'The volume of the circle is {math.pi * circleradius**3:.2f} cm^3')
print(f'The volume of the circle is {(math.pi * circleradius/100)**3:.2f} m^3')
print()
input()
