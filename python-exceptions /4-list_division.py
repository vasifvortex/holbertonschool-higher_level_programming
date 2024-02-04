#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    dev = 0
    for i in range(0, list_length):
        try:
            dev = my_list_1[i] / my_list_2[i]
            lst.append(dev)
        except ZeroDivisionError:
            print("division by 0")
            lst.append(0)
        except IndexError:
            lst.append(0)
            print("out of range")
        except TypeError:
            lst.append(0)
            print("wrong type")
        finally:
            pass
    return lst
