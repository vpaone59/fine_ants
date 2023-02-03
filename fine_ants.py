# Vincent Paone
# 
# expense tracking
import os
# pandas >>>>>>> csv
import pandas as pd
import numpy as np
import math

# gets the range of dates (oldest and most recent) and prints them out


def get_date_head_tail(data):

    oldest = data[len(data)-1]
    latest = data[0]
    print(
        f"VIEWING TRANSACTION DATE RANGE: {oldest} ---TO--- {latest}")
    return oldest, latest


def export(data):
    print("p")


# gets the first and last debit item from the debit column and then finds the total
def add_debit(data):
    rc = 0
    oc = len(data)-1
    recent_deb = data["Debit"][rc]
    oldest_deb = data["Debit"][oc]

    while math.isnan(recent_deb):
        rc = rc + 1
        recent_deb = data["Debit"][rc]

    while math.isnan(oldest_deb):
        oc = oc - 1
        oldest_deb = data["Debit"][oc]

    recent_deb_date = data["Date"][rc]
    oldest_deb_date = data["Date"][oc]

    print(
        f"**Debit:\nmost recent: ${recent_deb}\t{recent_deb_date}\noldest: ${oldest_deb}\t{oldest_deb_date}\n")
    debit_trans = data["Debit"]
    deb_total = debit_trans.sum()
    return round(deb_total, 2)


# gets the first and last credit item from the credit column and then finds the total
def add_credit(data):
    rc = 0
    oc = len(data)-1
    recent_cre = data["Credit"][rc]
    oldest_cre = data["Credit"][oc]

    while math.isnan(recent_cre):
        rc = rc + 1
        recent_cre = data["Credit"][rc]

    while math.isnan(oldest_cre):
        oc = oc - 1
        oldest_cre = data["Credit"][oc]

    recent_cre_date = data["Date"][rc]
    oldest_cre_date = data["Date"][oc]

    print(
        f"**Credit:\nmost recent: ${recent_cre}\t{recent_cre_date}\noldest: ${oldest_cre}\t{oldest_cre_date}\n")
    credit_trans = data["Credit"]
    cre_total = credit_trans.sum()
    return round(cre_total, 2)


def main():
    print('\nfine_ants.py...working...\n')
    directory = os.getcwd()
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # as long as the file is a CSV that contains the string "transactions" then it should work
            if f.endswith(".csv"):
                if "transactions" in f:
                    file = f
                    break
                else:
                    print(
                        f"CSV file {f} does not contain phrase \"transactions\".\nRecommended to name file 'transactions.csv")
            else:
                print("File is not of type CSV")

    # read the CSV file
    print(f"reading {file}...\n")
    myfile = pd.read_csv(file)

    # use only the date and debit/credit columns
    focus_deb = myfile[["Date", "Debit"]]
    focus_cre = myfile[["Date", "Credit"]]

    # get the last and most recent date in the date column
    oldest, latest = get_date_head_tail(myfile["Date"])
    print(f"Oldest Transaction Date--------- {oldest}")
    print(f"Last Transaction Date----------- {latest}")

    total_debit = add_debit(focus_deb)
    total_credit = add_credit(focus_cre)
    print(
        f"Total Debit Transactions from {oldest} to {latest} = ${total_debit}")
    print(
        f"Total Credit Transactions from {oldest} to {latest} = ${total_credit}")


if __name__ == '__main__':
    main()
