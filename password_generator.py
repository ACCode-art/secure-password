import random
import math


length = int(input("Length of Password: "))
lower_case = str(input("Contain lowercase? (y/n): "))
upper_case = (input("Contain uppercase? (y/n): "))
number = str(input("Contain numbers? (y/n): "))
special = str(input("Contain specials? (y/n): "))



new_list = [{'lower_case': lower_case}, {'upper_case': upper_case}, {'number': number}, {'special': special}]

new_filtered_list = {}


for el in new_list:
    for key in el:
        if el[key] == 'y':
            new_filtered_list.update(el)


filtered_keys = list(new_filtered_list.keys())

filtered_keys_length = len(filtered_keys)
    


def get_lower_case():
    return chr(97 + math.floor(random.random() * 26))

def get_upper_case():
    return chr(65 + math.floor(random.random() * 26))

def get_number():
    return chr(48 + math.floor(random.random() * 9))

def get_special():
    return chr(33 + math.floor(random.random() * 14))


all_functions = {
  "get_lower_case": get_lower_case,
  "get_upper_case": get_upper_case,
  "get_number": get_number,
  "get_special": get_special,
}



final_password = ''

def generate_password():
    final_password = ''

    for n in range(0, length, filtered_keys_length):
        for i in filtered_keys:
            
            final_password += all_functions[f'get_{i}']()
    
    print(final_password[0:length]) 




generate_password()


    



