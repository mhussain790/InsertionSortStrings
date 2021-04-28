"""
Author: Masud Hussain
Course: CS162
Assignment: 4C
"""


def insertion_sort(a_list):
    """
    insertion sort method that sorts a list of strings and returns
    a list of case-insensitive strings.

    :param a_list:
    :return: n/a
    """

    for i in range(1, len(a_list)):
        value = a_list[i]

        position = i - 1

        while position >= 0 and value.lower() < a_list[position].lower():
            a_list[position + 1] = a_list[position]
            position -= 1

        a_list[position + 1] = value

# new_list = ["mango", "john", "Robert", "apple", "banana"]
#
# insertion_sort(new_list)
#
# for i in range(len(new_list)):
#     print (new_list[i])
