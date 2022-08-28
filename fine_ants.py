# expense tracking

import time
import csv
import os
# pandas >>>>>>> csv
import pandas as pd
import numpy as np


def get_date_head_tail(data):
    print("get_date_head_tail...working...")

    earliest = data.head(1).values
    latest = data.tail(1).values
    print(
        f"VIEWING TRANSACTION DATE RANGE: {latest} ---TO--- {earliest}")


def export(data):
    print("p")


def add_debit(data):
    print("\nadd_debit...working...")

    debit_date_range = data["Date"]
    get_date_head_tail(debit_date_range)
    print(
        f"\n**Debit most recent: \n{data.head(1)}\noldest: \n{data.tail(1)}\n\n")
    debit_trans = data["Debit"]
    deb_total = debit_trans.sum()
    return round(deb_total, 2)


def add_credit(data):
    print("\nadd_credit...working...")

    credit_date_range = data["Date"]
    get_date_head_tail(credit_date_range)
    print(
        f"\n**Credit most recent: \n{data.head(1)}\noldest: \n{data.tail(1)}\n\n")
    credit_trans = data["Credit"]
    cre_total = credit_trans.sum()
    return (round(cre_total, 2))


def main():
    print('\nfine_ants.py...working...\n')
    myfile = pd.read_csv(os.getcwd() + "/fine_ants/transactions.csv")
    focus_deb = myfile[["Date", "Debit"]]
    focus_cre = myfile[["Date", "Credit"]]

    add_debit(focus_deb)

    add_credit(focus_cre)


if __name__ == '__main__':
    main()
