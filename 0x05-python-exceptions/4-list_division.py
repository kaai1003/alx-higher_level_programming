#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    div = 0
    div_list = [0 for _ in range(list_length)]
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div = 0.0
        except TypeError:
            print("wrong type")
            div = 0.0
        except IndexError:
            print("out of range")
            div = 0.0
        finally:
            div_list[i] = div
    return div_list
