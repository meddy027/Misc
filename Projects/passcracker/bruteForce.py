"""
Password brute-force algorithm
Python 3
"""
import string
from itertools import product
from time import time
from numpy import loadtxt

easy_dB = {'admin': 'admin'}

def menu():
    
    choice = int(input("""1) Add User
2) See all Users
3) BruteForce
0) exit\n> """
    ))

    if choice == 1:
        add_usr()
    elif choice ==2:
        show_all_usrs()
    elif choice == 3:
        username = input('\nEnter user to hack: ')
        start = time()
        bruteforce(username)
        end = time()
        print('Total time: %.2f seconds' % (end - start))
        print('\n')
        menu()

    elif choice == 0:
        print('\n---Goodbye---')
    else:
        print('\nIncorrect input')
        menu()

def product_loop(password, generator, username):
    for p in generator:
        if ''.join(p) == password:
            print('\n==================[+]SUCCESS[+]==================', '\nUSERNAME: ', username, 
            '\tPASSWORD:', ''.join(p))
            return ''.join(p)
    return False

def add_usr():
    usr = input("\nEnter username: ")
    if (usr in easy_dB.keys()):
        print('\nUser already exists\n')
    else:
        pwd = input("Enter password (5 characters only): ")
        if (len(pwd)== 5):

            easy_dB[usr] = pwd
            print('\nUSER CREATED\n')
            menu()
        else:
            print('\nInvalid password\nUSER NOT CREATED\n')
            menu()

def show_all_usrs():
    print('\n')
    print('________USERS________')
    for key in easy_dB.keys():
        print(key)
    print('\n')
    menu()


def bruteforce(username, max_nchar=5): #change max_nchar to accept larger pass

    password = easy_dB[username]

    print('\n1) Comparing with most common passwords / first names')
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('middle-names.txt', dtype=str)
    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]

    if len(cp) == 1:
        print('\n================[+]SUCCESS[+]=================', '\nUSERNAME: ', username, 
            '\tPASSWORD:', ''.join(cp))
        return cp
    if len(cn) == 1:
        print('\n=================[+]SUCCESS[+]==================', '\nUSERNAME: ', username, 
            '\tPASSWORD:', ''.join(cn))
        return cn
    
    if len(cnl) == 1:
       print('\n===================[+]SUCCESS[+]==================', '\nUSERNAME: ', username, 
            '\tPASSWORD:', ''.join(cnl))
       return cnl

    print('\n2) Digits Cartesian Product')
    for l in range(max_nchar, max_nchar + 1):
        generator = product(string.digits, repeat=int(l))
        print("\t...%d digit" % l)
        p = product_loop(password, generator, username)
        if p is not False:
            return p

    print('\n3) ASCII Lowercase + Digits')
    for l in range(max_nchar, max_nchar + 1):
        print("\t...%d char" % l)
        generator = product(string.ascii_lowercase + string.digits,
                            repeat=int(l))
        p = product_loop(password, generator, username)
        if p is not False:
            return p

    print('\n4) ASCII Uppercase/Lowercase + Digits')
    # If it fails, we start brute-forcing the 'hard' way
    # Same as possible_char = string.printable[:-5]
    all_char = string.ascii_uppercase + string.digits + string.ascii_lowercase# + string.punctuation

    for l in range(max_nchar, max_nchar + 1):
        print("\t...%d char" % l)
        generator = product(all_char, repeat=int(l))
        p = product_loop(password, generator, username)
        if p is not False:
            return p


# EXAMPLE
menu()
#bruteforce('Admin') # Try with 'abcde' or '12453' or 'zZZz9'