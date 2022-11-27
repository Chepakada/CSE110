import math

#m means mass
print('The acceleration due to gravity is taken as 9.8m/s^2')
print('All the quantities are in SI units, no need for unit ')
#print('Just to let you know, your object is falling in air.')
#m=float(input('Enter the mass of the body. '))
m=20
g=9.8
g1=24.79
e= 2.71828
#t=float(input('Enter the time the falling object has passes. '))
t=5
#rho=p is given by 1.3kg/m^3 for air
#p=float(input('Enter the density of the fluid. '))
p=2
#A=float(input('Please input the cross section area of the body. '))
A=52
#C=float(input('Input the drag constant for your object. It is 0.5 for sphere, 1.1 for cylinder on your side. '))
C=5
#c is the drag constant
c=((1/2)*p*A*C)
velocity_at_t1= math.sqrt(m*g1/c)*(1-math.exp((-math.sqrt(abs(m*g1*c)*t/m))))
velocity_at_t= math.sqrt(m*g/c)*(1-math.exp((-math.sqrt(abs(m*g*c)*t/m))))
print(f'The velocity of the object at time {t} is given by {velocity_at_t:.3f} m/s in Jupiter.')
print(f'The velocity of the object at time {t} is given by {velocity_at_t1:.3f} m/s in Jupiter.')
# Do this or die.

t=1
velocity_at_t2=0
while velocity_at_t2 < -velocity_at_t1:
    velocity_at_t2=math.sqrt(m*g1/c)*(1-math.exp((-math.sqrt(abs(m*g1*c)*(t+1)/m))))
    t=t+1
    print(velocity_at_t2)
    
