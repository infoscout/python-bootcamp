from core import test_helper


# Question 1
# ----------
# Given a list of numbers return a sorted list with only the unique elements.
def uniques_sorted(nums):
    # Write code here
    pass


# Question 2
# ----------
# Fill in: Dictionaries
#


# Question 3
# ----------
# Fill in: datetime module


def main():
    print "\nRunning uniques_sorted function..."
    test_helper(uniques_sorted([1, 2, 3]), [1, 2, 3])
    test_helper(uniques_sorted([0, 0]), [0])
    test_helper(uniques_sorted([5, 5, 12, 13, 15, 0, -1, 12]), [-1, 0, 5, 12, 13, 15])

if __name__ == '__main__':
    main()
