def welcome_user():
    print("""Welcome to the Time Calculator!
Please enter your time in format 'HH:MM PM/AM'""")
    time = input()
    print('Please enter time interval in format HH:MM')
    interval = input()
    print("Now you can enter the day of the week. If you don't want to - press Enter")
    weekday = input()
    return time, interval, weekday
