from core import test_helper


# Question 1
# ----------
# Given a list of numbers return a sorted list with only the unique elements.
def uniques_sorted(nums):
    return sorted(set(nums))


# Question 2
# ----------
# Given first name, last name, and age return a dictionary that has
# 3 items. The keys should be 'fname', 'lname', and 'age'.
# The values will be the function parameters. The first name and last name
# should be title case
def dict_profile(fname, lname, age):
    return {
        'fname': fname.title(),
        'lname': lname.title(),
        'age': age
    }


def main():
    print "\nRunning uniques_sorted function..."
    test_helper(uniques_sorted([1, 2, 3]), [1, 2, 3])
    test_helper(uniques_sorted([0, 0]), [0])
    test_helper(uniques_sorted([5, 5, 12, 13, 15, 0, -1, 12]), [-1, 0, 5, 12, 13, 15])

    print "\nRunning dict_profile function..."
    test_helper(dict_profile('walter', 'sobchak', 30), {'fname': 'Walter', 'lname': 'Sobchak', 'age': 30})
    test_helper(dict_profile('JEFF', 'leBowski', 0), {'fname': 'Jeff', 'lname': 'Lebowski', 'age': 0})
    test_helper(dict_profile('smokey', '', 89), {'fname': 'Smokey', 'lname': '', 'age': 89})

if __name__ == '__main__':
    main()
