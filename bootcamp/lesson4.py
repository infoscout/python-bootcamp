import datetime
import math

import requests

from core import test_helper


# Question 1
# ----------
# Using the datetime module return a datetime object with the year of 2015, the month of June, and the day of 1
def playing_with_dt():
    return datetime.datetime(year=2015, month=06, day=01)


# Question 2
# ----------
# Using the math module return pi
def playing_with_math():
    return math.pi


# Question 3
# ----------
# The following URL is public data set of demographic statistics by zip code in the city of New York
# url: https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json?accessType=DOWNLOAD
#
# Make a request to that address and inspect the contents. Return the number of unique demographic attributes in the
# data set as well as the percentage of ETHNICITY UNKNOWN formatted as a string with 2 significant figures.
# The return object should be a tuple data type
def explore_data():
    demo_attributes = []
    url = 'http://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json?accessType=DOWNLOAD'

    r = requests.get(url=url)
    json = r.json()
    meta = json['meta']
    view = meta['view']
    columns = view['columns']

    for column in columns:
        if column['name'] == 'PERCENT ETHNICITY UNKNOWN':
            avg = column['cachedContents']['average']
        if column['dataTypeName'] == 'number':
            demo_attributes.append(column['name'])

    num_attributes = len(set(demo_attributes))
    avg_formatted = '{:.4f}%'.format(float(avg))
    t = (avg_formatted, num_attributes)

    return t


def main():
    print "\nRunning playing_with_dt_one function..."
    test_helper(playing_with_dt(), datetime.datetime(2015, 06, 01))

    print "\nRunning playing_with_dt_one function..."
    test_helper(playing_with_math(), math.pi)

    print "\nRunning explore_data function..."
    test_helper(explore_data(), ('0.0039%', 46))

if __name__ == '__main__':
    main()
