 
 
 
 
 
import linecache
with open('life-expectancy.csv') as life_expt:
   

    #my_line is the list for putting all the lines of data for year provided by user.
    my_line=[]
    my_line2=[]
    # variable 'a' is counter for age and so is 'b', highest and lowest respectively
    a=0
    # n_high and n_low are variable responsible for getline to get the required line
    n_high=0
    n_low=0
    b=100000000000000000
    x=0
    
    drop_content=linecache.getline('life-expectancy.csv', 2)
    drop_content_splt=drop_content.split(',')
    dropped_age=float(drop_content_splt[2])
    dropped_year=int(drop_content_splt[2])
    print(dropped_age)
    next(life_expt)
    for num, line in enumerate(life_expt, 1):
    
        cln_lne=line.strip()
        splt_lne=cln_lne.split(',')
        age=float(splt_lne[3])
        year=int(splt_lne[2])
        cntry=splt_lne[0]
        gap_counter=0
        gap_counter2=0
        gap_age=0
        drop_year=int(year)
        drop_age= float(age)
        x=x+2
        while x!=num:
            drop_content=linecache.getline('life-expectancy.csv', num+2)
            drop_content_splt=drop_content.split(",")
            dropped_age1=drop_content_splt[-1]
            dropped_age=float(dropped_age)
            dropped_year=int(drop_content_splt[-2])
            if abs(drop_year-dropped_year)<2:
                if gap_age<abs(dropped_age-drop_age):
                    gap_age=2       #abs(dropped_age-drop_age)
                    gap_counter=splt_lne
                    gap_counter2=drop_content_splt
    print(gap_age)
        
    