import datetime
import math

from core import test_helper


# Question 1
# ----------
# Using the datetime module return a datetime object with the year of 2015, the month of June, and the day of 1
def playing_with_dt():
    return datetime.datetime(2015, 06, 01)


# Question 2
# ----------
# Using the math module return pi
def playing_with_math():
    return math.pi


def main():
    print "\nRunning playing_with_dt_one function..."
    test_helper(playing_with_dt(), datetime.datetime(2015, 06, 01))

    print "\nRunning playing_with_dt_one function..."
    test_helper(playing_with_math(), math.pi)

if __name__ == '__main__':
    main()
