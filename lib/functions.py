#!/usr/bin/env python3

def greet_programmer():
    pass 
    print("Hello, programmer!")

def greet(name):
    pass
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    pass
    print(f'Hello, {name}!')

def add(num1, num2):
    return num1 + num2
print(add(20,20))


def halve(number):
    if type(number) != int and type(number) != float:
        return None

    return number / 2
