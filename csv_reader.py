import csv
import sys
from random import seed
import gentemplate
import os
import sendmail
from random import shuffle
from random import randrange

RECEIVER_EMAIL = ['your_email_address']

SENDER_EMAIL = "no-reply-1@domain.com"
SUBJECT = "Hello"


class LaunchRoulette(object):

    def __init__(self, path):
        self.path = path

    def get_groups(self, grp):
        #print(grp)
        for ele in grp:
            employee = []
            htmlfile = str("group-{}.html".format(grp.index(ele)))
            #print("Group - {} ".format(grp.index(ele)))
            for emp in ele:
                employee.append(emp)
            employeename = [en.split(".")[0] for en in employee]
            print(employeename)
            email_content = gentemplate.html(employeename)
            return sendmail.sendmail(SUBJECT, email_content, employee, SENDER_EMAIL)


    def generate_sequence(self, tc):
        shuffle(tc)
        num_of_ppl = []
        arr = []
        x = 0
        if len(tc) < 4:
            print("ERROR: less than 4 employees")
            sys.exit()

        while x <= (len(tc)-4):
            num_of_ppl.append(randrange(3, 5, 1))
            x = sum(num_of_ppl)

        remaining_people = (num_of_ppl[-1] + (len(tc) - sum(num_of_ppl)))
        num_of_ppl[-1] = remaining_people

        for ele in num_of_ppl:
            arr.append(tc[:ele])
            del tc[:ele]

        return self.get_groups(arr)

    def read_csv(self):
        email_arr = []
        email_index = 1
        rownum = 0
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if rownum == 0:
                    header = row
                else:
                    email = row[email_index]
                    email_arr.append(email)
                rownum += 1
#        return email_arr
        return self.generate_sequence(email_arr)


if __name__ == '__main__':
    csv_file_name = 'employee.csv'
#   csv_file_name = sys.argv[1]
    all_email = LaunchRoulette(csv_file_name)
    all_email.read_csv()
