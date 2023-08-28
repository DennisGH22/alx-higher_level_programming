#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i] if i < len(my_list_1) else 0
                value_2 = my_list_2[i] if i < len(my_list_2) else 0

                if value_2 == 0:
                    raise ZeroDivisionError

                division_result = value_1 / value_2
                result.append(division_result)
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    except:
        pass
    finally:
        return result
