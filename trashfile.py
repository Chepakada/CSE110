import math
def script():
    def warning():
        war=input('do you want to go agian?(Y/N)').lower()
        if war=='y':
            script()
        else:
            quit
    def compute_area_rectangle(side,side1):
            ''' Compute area of rectangle
                input: 
                sides of rectangle
            output:
                area'''
            area=(side*side1)
            return area 
    def compute_area_square(side):
            '''Compute the area of square
                input:
                length
                output:
                area of square'''
            area=side**2 
            return area
    def compute_area_circle(side):
        '''Compute the area of circle
            input: 
            radius
            output:
            area'''
        area=math.pi*(side**2)
        return area
    def compute_area(shape, side, side1=0):
        if shape=='Rectangle':
            
            area=compute_area_rectangle(side, side1)
            return area
        elif shape=='square':
                 
            print(compute_area_square(side))
            
        elif shape=='circle':
            print(compute_area_circle(side))
           
    shape=input('What shape do you want?(RECTANGLE/CIRCLE/SQUARE)')
    if shape=='Rectangle':
        side=float(input('Enter a side of rectangle. '))
        side1=float(input('Enter the other side of rectangle'))
    elif shape=='square':
        side=float(input('Enter the side of square. '))
    elif shape=='circle':
        side=float(input('enter the radius of circle. '))
    
    compute_area(shape,side,side1=0)
script()