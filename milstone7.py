

f_c=input('Enter the unit you want to use.(F/C). ').lower()
t=float(input("Enter the air temperature. "))
v=0
#Do not use global variable, it can be changed by anyone which can be messy.
def farenhiet(t,v):
    windchill=35.74+0.6215*t-35.75*(v**0.16)+0.4275*t*(v**0.16)
    return windchill


def celcius(t):
    celc_wind=t*1.8+32
    return celc_wind

for i in range(5, 61, 5):

    if f_c=='f':
        wnd_chll=farenhiet(t,i)
        print(f'For windspeed {i} the wind chill is{wnd_chll:.2f}F at {t}F\' ')
        
    elif f_c=='c':
        celc_wndchll=celcius(t)
        wnd_chll=farenhiet(celc_wndchll,i)
    
        print(f'for windspeed {i}, the windchill is {wnd_chll:.2f}F at {t}C\'')
input()