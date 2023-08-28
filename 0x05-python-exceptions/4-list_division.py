#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):    
    D = [] #Dvision list
    for i in range (list_length):
        try:
            D.append(my_list_1[i]/my_list_2[i])
        except TypeError:
            D.append(0)
            print("wrong type")
        except IndexError:
            D.append(0)
            print("out of range")
        except ZeroDivisionError:
            D.append(0)
            print("division by 0")
    return (D)
