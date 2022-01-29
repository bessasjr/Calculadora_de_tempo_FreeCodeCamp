def add_time(start, duration, day=False):

    new_hour = None
    new_time_course = None
    new_minutes = None
    days_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_day = day
    
    #Início do horário
    time_base = start.split(':')
    time_hour = int(time_base[0])
    time_base_2 = time_base[1].split(' ')
    time_minutes = int(time_base_2[0])
    time_course = time_base_2[1]

    #Acréscimo do horário
    duration = duration.split(':')
    duration_hour = int(duration[0])
    duration_minutes = int(duration[1])

    new_time_hour = time_hour + duration_hour
    new_time_minutes = time_minutes + duration_minutes   

    if new_time_hour > 12 and new_time_hour < 24:
        h = new_time_hour - 12
        new_hour = h

        if time_course == 'AM':
            new_time_course = 'PM'

        if time_course == 'PM':
            new_time_course = 'AM'
    else:
        new_hour = new_time_hour
        new_time_course = time_course

    if new_time_hour > 24:
        t = new_time_hour / 24
        h_1 = str(t).split('.')
        h_2 = int(h_1[1][0])
        if h_2 < 5:
            h_2 = 5
            h_1[1] = str(h_2) 
            h_3 = '.'.join(h_1)
            t = round(float(h_3))
        else:
            t = round(t)
        #print(duration_hour//24)
        #print(duration_hour%24)

        s = (t-1)*24
        m = new_time_hour - s

        if m > 12:
            m = m -12
            new_hour = m
        else:
            new_hour = m
        
        tt = t * 2
        if time_course == 'PM':            
            if tt % 2 == 0:
                new_time_course = 'AM'
        if time_course == 'AM':
            if tt % 2 == 0:            
                new_time_course = 'PM'

    if new_time_minutes > 60:
        m = new_time_minutes - 60
        if m < 10:
            new_minutes = f'0{m}'
            new_hour = new_hour + 1
            if time_course == 'PM':
                new_time_course = 'AM'
            if time_course == 'AM':
                new_time_course = 'PM'
        else:
            new_minutes = m
            new_hour = new_hour + 1
    else:
        if new_time_minutes < 10:
            new_minutes = f'0{new_time_minutes}'
        else:
            new_minutes = new_time_minutes

    #d1 = 
    #print(t)

    if day != False:
        new_time = f'# Returns: {new_hour}:{new_minutes:2} {new_time_course}, {new_day}'
    else:
        new_time = f'# Returns: {new_hour}:{new_minutes:2} {new_time_course}'

    return new_time


#print(add_time("11:06 PM", "2:02"))
#print(add_time("3:00 PM", "3:10"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"))
#print(add_time("6:30 PM", "205:12"))

print(add_time("10:40 PM", "70:30", "Monday"))
print(add_time("8:00 PM", "192:00", "Monday"))

#print(add_time("3:30 PM", "2:12"))
#print(add_time("11:55 AM", "3:12"))
#print(add_time("9:15 PM", "5:30"))
#print(add_time("11:40 AM", "0:25"))
#print(add_time("2:59 AM", "24:00"))
#print(add_time("11:59 PM", "24:05"))