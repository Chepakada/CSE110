#
import math
def script():
    '''script of whole code'''
    print()
    def compute_area_rectangle(side,side1):
            ''' Compute area of rectangle
                input: 
                sides of rectangle
            output:
                area'''
            area=(side*side1)
            return area 
    def compute_area_square(side,side1):
            '''Compute the area of square
                input:
                length
                output:
                area of square'''
            area=side**2 
            return area
    def compute_area_circle(side,side1):
        '''Compute the area of circle
            input: 
            radius
            output:
            area'''
        area=math.pi*(side**2)
        return area
            


    shape=input('enter the shape that you want. (CIRCLE/SQUARE/RECTANGLE)').lower()
    if shape=='rectangle':
        side=float(input(f'Enter one side of rectangle'))
        side1=float(input(f'enter the other side of the rectangle'))
       
        
        #areaa=compute_area_rectangle(side, side1 )
    elif shape == 'square':
        side= float(input('Enter the length of the square. '))
        
        #areaa=compute_area_square(side)
    elif shape=='circle':
        side=float(input('Enter the radius of the circle. '))
        
        #areaa=compute_area_circle(side)
    '''
    print(f'the area of {shape} is {areaa}')
    choice=input('do you want to continue?(Y/N) ').lower()
    if choice=='n':
        return
    elif choice=='y':
        script()
    else:
        choice=input('do you want to go again?(Y/N) ').lower()
    '''



    def compute_area(shape, side, side1=0):
        if shape=="rectangle":
            print(compute_area_rectangle(side,side1))
        elif shape=='square':
            print(compute_area_square(side))
            
        elif shape=='circle':
            print(compute_area_circle(side))
        else:
            script()

        
    compute_area(shape, side, side1)
script()
    
