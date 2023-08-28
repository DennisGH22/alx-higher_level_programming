#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    division_results = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError):
            result = 0

            if isinstance(my_list_1[i], (str, int)) or isinstance(my_list_2[i], (str, int)):
                print("Error: ", end="")

                if isinstance(my_list_1[i], str) or isinstance(my_list_2[i], str):
                    print("wrong type", end="")

                if isinstance(my_list_2[i], int) and my_list_2[i] == 0:
                    print("division by 0", end="")

                if i >= len(my_list_1) or i >= len(my_list_2):
                    print("out of range", end="")

                print()
        finally:
            division_results.append(result)

    return division_results
