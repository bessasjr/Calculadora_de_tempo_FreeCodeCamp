def add_time(start, duration, day=False):

    new_hour = None
    new_time_course = None
    new_minutes = None
    days_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_day = None
    hour_more = None
    days_more = None
    
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

    if duration_hour > 12:
        hour_inteiro = duration_hour//24
        hour_restante = duration_hour%24
        hour_restante_2 = hour_restante//12
        if hour_restante_2 == 1:
            hour_restante_2 = 0.5
        else:
            hour_restante_2 = 0
        hour_restante_3 = hour_restante%12
        days_more = hour_inteiro + hour_restante_2
        new_hour = time_hour + hour_restante_3
        
    if duration_hour < 12:
        hour_more = duration_hour
        new_hour = time_hour + duration_hour
        
    # Calculando a hora
    if new_hour > 12:
        new_hour = new_hour - 12
    else:
        pass

    # Calculando os minutos
    new_minutes = time_minutes + duration_minutes
    if new_minutes > 60:
        tt = new_minutes//60
        new_hour = new_hour + tt
        tw = new_minutes%60
        new_minutes = tw
        
    if new_minutes < 60:
        pass
    if new_minutes < 10:
        new_minutes = f'0{new_minutes}'
    else:
        pass

    # Calculando o período
    print(days_more)
    print(time_hour)
    if days_more != None:
        c = days_more + time_hour
        if c >= 12:
            c = c//12
            if time_course == 'AM':
                if c%2 == 0:
                    new_time_course = 'AM'
                if c%2 != 0:
                    new_time_course = 'PM'
            if time_course == 'PM':
                if c%2 == 0:
                    new_time_course = 'PM'
                if c%2 != 0:
                    new_time_course = 'AM'
        else:
            new_time_course = time_course
        if time_hour < 12 and new_hour == 12:
            if time_course == 'AM':
                new_time_course = 'PM'
            if time_course == 'PM':
                new_time_course = 'AM'
    if hour_more != None:
        c = hour_more + time_hour
        if c >= 12:
            c = c//12
            if time_course == 'AM':
                if c%2 == 0:
                    new_time_course = 'AM'
                if c%2 != 0:
                    new_time_course = 'PM'
            if time_course == 'PM':
                if c%2 == 0:
                    new_time_course = 'PM'
                if c%2 != 0:
                    new_time_course = 'AM'
        else:
            new_time_course = time_course
        if time_hour < 12 and new_hour == 12:
            if time_course == 'AM':
                new_time_course = 'PM'
            if time_course == 'PM':
                new_time_course = 'AM'


    #print(day)
    day_value = days_week.index(day)
    #print(day_value)

#    if new_hour_inteiro < 7:
#       print(int(new_hour_inteiro))
#
#    if new_hour_inteiro > 7:
#        n = (new_hour_inteiro % 7)
#        n = day_value + n
#        new_day = days_week[n]
#        print(n)        


    if day != False:
        day_value = days_week.index(day)

        new_time = f'# Returns: {new_hour}:{new_minutes:2} {new_time_course}, {new_day}'
    else:
        new_time = f'# Returns: {new_hour}:{new_minutes:2} {new_time_course}'

    return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20", "Tuesday"))
print(add_time("6:30 PM", "205:12"))

print(add_time("10:40 PM", "70:30", "Friday"))
#print(add_time("8:00 PM", "192:00", "Sunday"))
#
#print(add_time("11:06 PM", "2:02"))