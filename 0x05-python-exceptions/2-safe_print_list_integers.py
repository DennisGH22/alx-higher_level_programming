#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in range(my_list):
            try:
                print("{:d}".format(element), end="")
                count += 1

                if count == x:
                    break

            except ValueError:
                continue
    except Exception:
        pass
    finally:
        print()
        return count
