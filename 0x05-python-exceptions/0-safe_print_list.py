#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count < x:
                print("{}".format(element), end="")
                count += 1
            else:
                break
    except Exception:
        pass
    finally:
        print()
        return count
