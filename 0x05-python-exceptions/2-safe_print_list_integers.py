#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0

        for element in my_list:
            try:
                print("{:d}".format(element), end='')
                count += 1
            except (ValueError, TypeError):
                pass

            if count == x:
                break
    except Exception:
        pass
    finally:
        print()
        return count
