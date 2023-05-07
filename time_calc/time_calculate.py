def add_time(start, duration, weekday=''):
    take_start_minutes = to_minutes_converter(pm_am_converter(start))
    take_duration_minutes = to_minutes_converter(duration)
    days, hours, minutes, time_format = min_converter(take_start_minutes + take_duration_minutes)
    new_time = information(days, hours, minutes, time_format, weekday)
    return new_time

def number_day_week(day):
    '''Принимает день в виде строки и возвращает целое число - по порядку этого дня в неделе
    '''
    match day.lower():
        case 'monday':
            return 1
        case 'tuesday':
            return 2
        case 'wednesday':
            return 3
        case 'thursday':
            return 4
        case 'friday':
            return 5
        case 'saturday':
            return 6
        case 'sunday':
            return 7
        
def weekday_number(num):
    '''Принимает номер дня в неделе, возвращает его название
    '''
    match num % 7:
        case 0:
            return 'Sunday'
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'

        

def min_converter(min: int) -> str:
    ''' Принимает количество минут и возвращает дни, часы и минуты
    '''
    days = min // (24 * 60)
    hours = (min % (24 * 60)) // 60
    minutes = min % 60
    time_format = 'AM' if hours < 12 else "PM"
    hours = hours % 12 if hours not in (0, 12) else 12
    return days, hours, minutes, time_format


def to_minutes_converter(time: str) -> int:
    ''' Принимает строку из часов и минут вида "Hours:Minutes" и возвращает количество минут в виде целого числа
    '''
    h, m = map(int, time.split(":"))
    res = h * 60 + m
    return res

def pm_am_converter(s: str) -> str:
    ''' Функция принимает время в виде строки в формате "Hours:Minutes PM/AM" и возвращает строку в формате 24h
    '''
    time, c = s.split()
    if c == 'AM':
        return time
    else:
        h, m = map(int, time.split(":"))
        res = f'{h + 12}:{m}'
        return res


def information(days, hours, minutes, time_format, weekday):
    if weekday:
        week = f', {weekday_number(days + number_day_week(weekday))}'
    if days == 0:
        finish = ''
    elif days == 1:
        finish = ' (next day)'
    else:
        finish = f' ({days} days later)'

    return f'{hours}:{str(minutes).rjust(2, "0")} {time_format}{week if weekday else weekday}{finish}'.strip()



# a = to_minutes_converter("205:12")
# b = to_minutes_converter("18:30")
# print(b)
# print(min_converter(a + b))

print(add_time("3:00 PM", "3:10") == '6:10 PM')
print(add_time("11:30 AM", "2:32", "Monday") == '2:02 PM, Monday')
print(add_time("11:43 AM", "00:20") == '12:03 PM')
print(add_time("10:10 PM", "3:30") == '1:40 AM (next day)')
print(add_time("11:43 PM", "24:20", "tueSday") == '12:03 AM, Thursday (2 days later)')
print(add_time("6:30 PM", "205:12") == '7:42 AM (9 days later)')
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("2:59 AM", "24:00", "saturDay"))