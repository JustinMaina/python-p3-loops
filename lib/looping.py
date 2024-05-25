#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
        if count == 0:
            print("Happy New Year!")
            break
happy_new_year()


def square_integers(int_list):
    squared_ints = [ints ** 2 for ints in int_list]
    return squared_ints

square_integers([1, 2, 3, 4, 5])       
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()            