from core import test_helper


# Question 1
# ----------
# Given a string, return a string of the form "Open the pod bay doors, <string>."


def sayings(word):
    # Write code here
    pass

# Question 2
# ----------
# Given an int which is the count of donuts, return a string
# of the form "Number of donuts: <cnt>", where <cnt> is the number
# passed in. However, if the count is 10 or more, then use the word "many"
# instead of the actual count. So donuts(5) returns "Number of donuts: 5" and
# donuts(27) returns "Number of donuts: many"


def donuts(cnt):
    # Write code here
    pass


# Question 3
# -----------
# Given a meal cost and percent tip determine the total price for a dinner.
# A 5.5% sales tax should be added to the meal cost and the tip should be
# calculated based off that total. Return a formatted string which contains
# dollars and cents. For example $27.52


def dinner_calculator(meal_cost, pct_tip):
    # Write code here
    pass


def main():
    print "\nRunning sayings function..."
    test_helper(sayings("HAL"), "Open the pod bay doors, HAL.")
    test_helper(sayings("Daisy"), "Open the pod bay doors, Daisy.")
    test_helper(sayings("Mr. Trump"), "Open the pod bay doors, Mr. Trump.")

    print "\nRunning donuts function..."
    test_helper(donuts(4), 'Number of donuts: 4')
    test_helper(donuts(9), 'Number of donuts: 9')
    test_helper(donuts(10), 'Number of donuts: many')
    test_helper(donuts(99), 'Number of donuts: many')

    print "\nRunning dinner_calculator function..."
    test_helper(dinner_calculator(44.50, 0.15), '$53.99')
    test_helper(dinner_calculator(100.00, 0.20), '$126.60')

if __name__ == '__main__':
    main()
