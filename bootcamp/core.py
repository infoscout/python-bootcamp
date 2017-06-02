def say_hello():
    print "\n* Hello InfoScout Team!\n"


def test_helper(got, expected):
    if got == expected:
        prefix = 'Correct!'
    else:
        prefix = 'Fail!'
    print " {prefix}  got: {got} expected: {expected}".format(prefix=prefix, got=got, expected=expected)
