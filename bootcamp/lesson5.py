import datetime
import csv


# Question 1
# ----------
# Using the csv data file users.csv aggregate app users as well as registration date by month. The count of app
# users should be one dictionary while the count of registration month should be another dictionary. There will be
# no checking or test harness so simply print your results to the console.
# Example:
# d1 = {
#    'RECEIPT_HOG': 3325,
#    'SHOPAROO': 38,
#    'RECEIPT_LOTTERY': 820,
#    'RECEIPT_BIN': 3208
# }
# d2 = {
#    'Jan': 3852,
#    'Feb': 38525,
#    etc...
# }
def bigdata():
    apps_dict = {}
    reg_dict = {}
    file_path = '/Users/df/isc/python-bootcamp-pv/data/users.csv'

    with open(file_path, 'r') as csvreader:
        reader = csv.reader(csvreader)
        for row in reader:
            user_id, verified, app_id, state, reg_str = row
            if app_id in apps_dict:
                apps_dict[app_id] += 1
            else:
                apps_dict[app_id] = 1

            reg_dt = datetime.datetime.strptime(reg_str, "%Y-%m-%d %H:%M:%S")
            reg_month = reg_dt.strftime("%b")

            if reg_month in reg_dict:
                reg_dict[reg_month] += 1
            else:
                reg_dict[reg_month] = 0

    print "\nCount by Apps\n{apps_dict}".format(apps_dict=apps_dict)
    print "\nCount by Registration Month\n{reg_dict}\n".format(reg_dict=reg_dict)


def main():
    bigdata()

if __name__ == '__main__':
    main()
