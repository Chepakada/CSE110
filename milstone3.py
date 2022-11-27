from PIL import Image
'''
image_original = Image.open("cse110_images/beach.jpg")
#image_original.show()
pixels_original=image_original.load()
width, height=image_original.size
r, g, b=pixels_original[100,200]
print(f'{r=} {b=} {g=}')
pixels_original[100,201]=(9,0,0)
pixels_original[100,202]=(9,0,0)
pixels_original[100,203]=(9,0,0)
pixels_original[100,204]=(9,0,0)
pixels_original[100,205]=(9,0,0)
image_original.show()
'''

image_background = Image.open("cse110_images/desert.jpg")
pixels_background = image_background.load()
#image_background.show()
image_replaced = Image.open("cse110_images/hiker.jpg")
pixels_replaced = image_replaced.load()
#print(pixels_replaced[10,20])

for x in range(0, 800):
    for y in range(0,600):
        (r,g,b)=pixels_replaced[x,y]
        #pixels_replaced[x,y]=(r,g,255)
        #if pixels_replaced[x,y]== (44, 207, 64):
        if r<100 and g>110 and b<100:
            pixels_replaced[x,y]= pixels_background[x,y]
            r,g,b=pixels_replaced[x,y]
            pixels_replaced[x,y]=(r,g,100)
            for y in range(10,30):
                pixels_replaced[10,y]=(100,100,100)
               # for x in range(10,20):
                #    pixels_replaced[x,15]=(100,100,100)

image_replaced.show()



image_replaced.save('hiking_in_desert1.jpg')
'''
image_background1=Image.open('hiking_in_desert.jpg')
image_replaced1=Image.open('cse110_images/penguin.jpg')
pixels_background1=image_background1.load()
pixels_replaced1=image_replaced1.load()

for x in range(0, 800):
    for y in range(0,600):
        #(r,g,b)=pixels_replaced[x,y]
        #pixels_replaced[x,y]=(r,g,255)
        if pixels_replaced1[x,y]== (44, 207, 64):
            pixels_replaced1[x,y]= pixels_background1[x,y]

image_replaced1.show()
#print(pixels_replaced1[20,20])
'''
