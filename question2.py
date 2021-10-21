"""
#
File    :question2.py
Created :07/10/2021
Author  : Eoin O'Mahony
"""
import random
import pytest

if __name__ == '__main__':
    # create the lists of names
    names_wk1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]
    names_wk2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]

    numbers_wk1 = random.sample(range(1, 21), 10)
    numbers_wk2 = random.sample(range(1, 21), 10)

    # create dict for wk1 results
    res_wk1 = (list(zip(names_wk1, numbers_wk1)))
    res_wk1_dict = dict(res_wk1)
    print("Week 1 results: " + str(res_wk1_dict))

    # create dict for wk2 results
    res_wk2 = (list(zip(names_wk2, numbers_wk2)))
    res_wk2_dict = dict(res_wk2)
    print("Week 2 results: " + str(res_wk2_dict))

    # create a list of all names including duplicates
    # and a list to store unique names
    all_names = names_wk2 + names_wk1
    unique_names = list(set(all_names))
    print("All Unique names: " + str(unique_names))

    # Find the length of the list for the loop
    names_number = len(all_names) - 1
    multiple_entries = []
    # iterate through the list to find multiples
    for i in range(names_number):
        x = all_names[i]
        if all_names.count(x) > 1:
            multiple_entries.append(x)
    # create a set to find who entered more than once
    unique_multiple_entries = list(set(multiple_entries))
    print("Multiple entries: " + str(unique_multiple_entries))

    # find the most common numbers
    all_numbers = numbers_wk1 + numbers_wk2
    all_numbers.sort()
    totals_dict = {}
    d_key = []
    d_value = []
    for i in range(1, 20):
        x = all_numbers[i]
        total = all_numbers.count(i)
        d_key.append(x)
        d_value.append(total)
    totals_dict = dict(zip(d_key, d_value))
    print(totals_dict)

    print(max(totals_dict, key=totals_dict.get))
    # What I couldn't find was how to get multiple key values from the dictionary

    # iterate through the names that entered both weeks
    for i in unique_multiple_entries:
        if res_wk1_dict.get(i) == res_wk2_dict.get(i):
            print(str(i) + " had the same number both weeks")
        else:
            print(str(i) + " had different numbers both weeks")

