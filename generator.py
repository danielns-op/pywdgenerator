import characters as char
from time import sleep
from random import randint, choice


def get_letters():
    while True:
        try:
            num_letters = int(input('\tHow many letters would you like: '))
            return num_letters
        except ValueError:
            print('[ERROR] Enter only number')
            sleep(1)
            
    
def get_symbols():
    while True:
        try:
            num_symbols = int(input('\tHow many symbols would you like: '))
            return num_symbols
        except ValueError:
            print('[ERROR] Enter only number')
            sleep(1)

          
def get_numbers():
    while True:
        try:
            num_numbers = int(input('\tHow many numbers would you like: '))
            return num_numbers
        except ValueError:
            print('[ERROR] Enter only number')
            sleep(1)


def generating_pwd():
    pwd_list = []
    pwd = ''
    quant_letters = get_letters()
    quant_symbols = get_symbols()
    quant_numbers = get_numbers()
    
    for letter in range(1, quant_letters + 1):
        ch_letter = choice(char.letters)
        pwd_list.append(ch_letter)
    
    for symbol in range(1, quant_symbols + 1):
        ch_symbol = choice(char.symbols)
        index = randint(0, len(pwd_list) - 1)
        pwd_list.insert(index, ch_symbol)
    
    for number in range(1, quant_numbers + 1):
        ch_number = choice(char.numbers)
        index = randint(0, len(pwd_list) - 1)
        pwd_list.insert(index, ch_number)
    
    print('processing', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    
    for value in pwd_list:
        pwd += value
        
    return pwd
    