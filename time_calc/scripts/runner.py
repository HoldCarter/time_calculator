from time_calc.time_calculate import add_time
from time_calc.welcome import welcome_user


def main():
    time, interval, weekday = welcome_user()
    print(add_time(time, interval, weekday))


if __name__ == '__main__':
    main()
