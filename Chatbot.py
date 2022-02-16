# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 06:05:53 2022

@author: Vivek Prakash Upreti
"""

def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}')
    print(f'I was created in {birth_year}')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    
    while True:
        n = int(input())
        if n>=4:
            print('Please Try Again.')
            continue
        elif n==1 or n==2 or n==3:
            print('Completed, have a nice day!')
            break
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Quantum', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
