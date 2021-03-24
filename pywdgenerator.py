# pywdgenerator.py                           #
#                                            #
# Python password generator                  #
# ------------------------------------------ #
#  Author: Daniel Noronha                    #
#   email: danielnoronha.sh@gmail.com        #
#  GitHub: https://github.com/danielns-op    #
# ------------------------------------------ #
# Version: 1.0                               #
#    Date: 23/01/2021                        #
# ########################################## #
import generator as gen
import os


def start():
    logo = '''
  ____           __        __  ____  
 |  _ \   _   _  \ \      / / |  _ \ 
 | |_) | | | | |  \ \ /\ / /  | | | |
 |  __/  | |_| |   \ V  V /   | |_| |
 |_|      \__, |    \_/\_/    |____/ 
          |___/                      
   ____                                        _                  
  / ___|   ___   _ __     ___   _ __    __ _  | |_    ___    _ __ 
 | |  _   / _ \ | '_ \   / _ \ | '__|  / _` | | __|  / _ \  | '__|
 | |_| | |  __/ | | | | |  __/ | |    | (_| | | |_  | (_) | | |   
  \____|  \___| |_| |_|  \___| |_|     \__,_|  \__|  \___/  |_|   
'''
    print('-=' * 40)
    print('Welcome to the password generator...')
    print(logo)
    print('-=' * 40)
            

def menu():
    start()
    print('\nDefine your password characteristics.')
    result_pwd = gen.generating_pwd()
    
    return result_pwd


in_execution = True
while in_execution:
    if __name__ == '__main__':
        password = menu()
        print(f'\n\n----> Here is your password: {password}\n')
        print('-=' * 40)

        q_exit = str(input('Generate another password? [S/n]: ')).strip().lower()
        if q_exit == 'n':
            in_execution = False
        else:
            print('Invalid option, running the program.')
            os.system('cls') if os.name == 'nt' else os.system('clear')
