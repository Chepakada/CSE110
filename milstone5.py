import linecache
with open('life-expectancy.csv') as life_expt:
    user_year=int(input('Enter the year you want to know about.' ))
    user_country=(input('Enter the country you want to know. '))

    #my_line is the list for putting all the lines of data for year provided by user.
    my_line=[]
    my_line2=[]
    # variable 'a' is counter for age and so is 'b', highest and lowest respectively
    a=0
    # n_high and n_low are variable responsible for getline to get the required line
    n_high=0
    n_low=0
    b=100000000000000000
    

    next(life_expt)
    for num, line in enumerate(life_expt, 1):
    
        cln_lne=line.strip()
        splt_lne=cln_lne.split(',')
        age=float(splt_lne[3])
        year=int(splt_lne[2])
        cntry=splt_lne[0]
        if a<age:
            a=age
            n_high=num     
        if b>age:
            b=age
            n_low=num
    
       
        



        #here, year is the year in every line of data 
        #user_year is the year input by user
        #this if statement following add all the lines of data with year which matches to year provided by user 
        if user_year==year:
            my_line.append(splt_lne)







        if cntry.lower()==user_country.lower():
            my_line2.append(splt_lne)

        '''
        print(splt_lne)
        a=a+1
        if a==5:
            break
        '''
    


    content_high=linecache.getline('life-expectancy.csv', n_high+1)
    content_high_split=content_high.split(",")
    print(f'THe  overall highest life expectancy is of {content_high_split[0]} at {a} on year {content_high_split[2]}.')
    content_low=linecache.getline('life-expectancy.csv', n_low+1)
    content_low_split=content_low.split(",")
    print(f'the overall lowest life expectancy is {content_low_split[0]} at {b} on year {content_low_split[2]}.')




    #here, agevar are variables used to calculate maximum and minimum years
    agevar_h=0
    agevar_l=100000
    cntvar_h=0
    cntvar_l=0
    total=0
    cntr=0

  

    for line2 in my_line:
        cntvar_h=float(line2[3])
        cntvar_l=float(line2[3])
        #here, the total adds all the years in the list my_line
        total += cntvar_h
        #here, cntr adds the number of lines in th list my_line
        cntr=cntr+1
        if agevar_h<cntvar_h:
            agevar_h=cntvar_h
            cntry_h=line2[0]



        if agevar_l>cntvar_l:
            agevar_l=cntvar_l
            cntry_l=line2[0]


    print(f'the overall average for the year {user_year} is {total/cntr:.2f}')
    print(f'the maximum life expectancy is {agevar_h} in {user_year} and in country {cntry_h}.')
    print(f'the minimun life expectancy is {agevar_l} in {user_year} and in country {cntry_l}.' )






      #here, agevar are variables used to calculate maximum and minimum years
    agevar_h2=0
    agevar_l2=100000
    cntvar_h2=0
    cntvar_l2=0
    total2=0
    cntr2=0

  

    for line22 in my_line2:
        cntvar_h2=float(line22[3])
        cntvar_l2=float(line22[3])
        #here, the total adds all the years in the list my_line2
        total2 += cntvar_h2
        #here, cntr adds the number of lines in th list my_line2
        cntr2=cntr2+1
        if agevar_h2<cntvar_h2:
            agevar_h2=cntvar_h2
            cntry_h2=line22[0]
            year_h2=line22[2]


        if agevar_l2>cntvar_l2:
            agevar_l2=cntvar_l2
            cntry_l2=line22[0]
            year_l2=line22[2]


    print(f'the overall average for the country {user_country} is {total2/cntr2:.2f}')
    print(f'the maximum life expectancy is {agevar_h2} in {year_h2} and in country {user_country}.')
    print(f'the minimun life expectancy is {agevar_l2} in {year_l2} and in country {user_country}.' )
