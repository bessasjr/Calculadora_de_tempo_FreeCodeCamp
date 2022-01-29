def add_time(start, duration, day=False):

    days_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_hour_0 = 0
    new_hour = None
    new_time_course = None
    new_minutes = None
    new_day = None
    days_more = 0
    hours_more = None
    days_count = 0

    # Início do horário
    time_base = start.split(':')
    time_hour = int(time_base[0])
    time_base_2 = time_base[1].split(' ')
    time_minutes = int(time_base_2[0])
    time_course = time_base_2[1]

    # Acréscimo do horário
    duration = duration.split(':')
    duration_hour = int(duration[0])
    duration_minutes = int(duration[1])

    new_minutes = time_minutes + duration_minutes

    if new_minutes >= 60:
        new_hour_0 = new_hour_0 + 1
        new_minutes = new_minutes - 60

    if new_minutes < 10:
        new_minutes = f'0{new_minutes}'

    if duration_hour > 12:
        days_more = duration_hour//24
        hours_more = duration_hour%24
    else:
        hours_more = duration_hour

    hours_more_bruto = hours_more

    if hours_more > 12:
        hours_more = hours_more - 12
    
    new_hour = new_hour_0 + time_hour + hours_more
    if new_hour > 12:
        new_hour = new_hour - 12


    if time_hour + hours_more_bruto < 24:
        if time_hour + hours_more_bruto != new_hour:
            if time_course == 'AM':
                new_time_course = 'PM'
            if time_course == 'PM':
                new_time_course = 'AM'
        else:
            new_time_course = time_course
    else:
        value_0 = hours_more_bruto - 12
        if value_0 != new_hour:
            if time_course == 'AM':
                new_time_course = 'AM'
            if time_course == 'PM':
                new_time_course = 'PM'
        else:
            new_time_course = time_course


    if time_course == 'PM' and (time_hour + duration_hour) > 12 < 24:
        days_count = 1 + days_more
    else:
        days_count = days_more

    if day != False:
        day = day.capitalize()
        if days_count == 0:
            new_day = day
            new_time = f'{new_hour}:{new_minutes:2} {new_time_course}, {new_day}'
            
        else:
            #print(days_count)
            if days_count >= 1:
                d = days_week.index(day) + 1
                #print(d)
                s = (d + (days_count%7))
                #print(s)
                if s > 7:
                    s = s - 7
                else:
                    pass
                new_day = days_week[s-1]

        if days_count == 1:
            new_time = f'{new_hour}:{new_minutes:2} {new_time_course}, {new_day} (next day)'
        if days_count > 1:
            new_time = f'{new_hour}:{new_minutes:2} {new_time_course}, {new_day} ({days_count} days later)'

    else:
        if days_count == 0:
            new_time = f'{new_hour}:{new_minutes:2} {new_time_course}'
        if days_count == 1:
            new_time = f'{new_hour}:{new_minutes:2} {new_time_course} (next day)'
        if days_count > 1:
            new_time = f'{new_hour}:{new_minutes:2} {new_time_course} ({days_count} days later)'

    return new_time

#print(add_time("3:00 PM", "3:10"))
#print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20", "tuesday"))
#print(add_time("6:30 PM", "205:12"))
#
#print(add_time("10:40 PM", "70:30", "Friday")) #9:10
#print(add_time("8:00 PM", "192:00", "Sunday"))
#print(add_time("11:06 PM", "2:02"))
#
#print(add_time("8:16 PM", "466:02", "tuesday"))
#
#'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'