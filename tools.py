# import only system from os
from os import system, name


# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for linux or mac
    else:
        _ = system('clear')
