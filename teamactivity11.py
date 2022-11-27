with open("hr_system.txt") as hr_st:
    next(hr_st)
    for line in hr_st:
        clean_list=line.strip()
        file_list=clean_list.split(" ")
        name=file_list[0]
        job_title=file_list[2]
        salary=int(file_list[3])/24
        id=file_list[1]
        bon_pcl=salary+1000
        if job_title=='Engineer':
            print(f'{name:2} (Id: {id}), {job_title} - {bon_pcl}' ) 
            