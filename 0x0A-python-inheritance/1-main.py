#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.print_sorted()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(-2)
print(my_list)
my_list.print_sorted()
print(my_list)
try:
    new_list = my_list.print_sorted()
except Exception as e:
    print(e)
try:
    print(new_list)
except Exception as e:
    print(e)
