"""
#
File    :lotto_example.py
Created :21/10/2021
Author  : Eoin O'Mahony
"""

import random


class Lotto:
    def lotto(self, highest):
        # create the lists of names
        if highest <= 10:
            print("Should return false" + str(highest))
            return "Failed"
        else:
            names_wk1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]
            names_wk2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]

            numbers_wk1 = random.sample(range(1, highest), 10)
            numbers_wk2 = random.sample(range(1, highest), 10)
            print(numbers_wk1)

            # create dict for wk1 results
            res_wk1 = (list(zip(names_wk1, numbers_wk1)))
            res_wk1_dict = dict(res_wk1)
            print("Week 1 results: " + str(res_wk1_dict))

            # create dict for wk2 results
            res_wk2 = (list(zip(names_wk2, numbers_wk2)))
            res_wk2_dict = dict(res_wk2)
            print("Week 2 results: " + str(res_wk2_dict))
            return "Passed"

#x = Lotto
#x.lotto(Lotto, 11)