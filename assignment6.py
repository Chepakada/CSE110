
print('Please rate every question from 1-10, 1 being the least.')
loan=int(input('How large is your loan?'))
history=int(input('How good is your credit history?'))
income=int(input('How high is your income?'))
downpay=int(input('How large is your down payment?'))
case1=[history,income]
if loan>=5:
    if history>=7 and income>=7:
        decison='Yes'
    elif history>=7 or income>=7:
        if downpay>=5:
            decison="Yes"
        else:
            decison="No"
    else:
        decison='No'
else:
    if history<4:
        decison="No"
    else:
        if income>=7 or history>=7:
            decison='Yes'
        elif income>=4 and downpay>=4:
            decison="Yes"
        else:
            decison="No"
if decison=="Yes":
    pn='Your loan is approved'
else:
    pn='Your loan is denied'
print(pn)


