from core import test_helper


# Question 1
# ----------
# Given a list of strings, return the count of the number of strings where the string length
# is 2 or more and the first and last chars of the string are the same.
def match_ends(words):
    # Write code here
    pass


# Question 2
# ----------
# Given a list of strings, return a list with the strings in sorted order,
# except group all the strings that begin with 'x' first. Example:
# ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
def sort_x(words):
    # Write code here
    pass


# Question 3
# ----------
# Given a list of numbers write a function to sum every element in the list. Return the sum
#
def sum_elements(nums):
    # Write code here
    pass


def main():
    print '\nRunning match_ends function...'
    test_helper(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test_helper(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test_helper(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print '\nRunning sort_x function...'
    test_helper(sort_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test_helper(sort_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test_helper(sort_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print'\nRunning sum_elements function...'
    test_helper(sum_elements([1, 2, 3, 4, 5]), 15)
    test_helper(sum_elements([0, 0]), 0)
    test_helper(sum_elements([0, 1, -1, 1]), 1)

if __name__ == '__main__':
    main()

