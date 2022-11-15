from string import ascii_letters, digits
from random import choices
from typing import Optional



def generate_password(pass_len: int) -> Optional[str]:
    if not isinstance(pass_len, int): 
        print(f'Введите число. Вы ввели {pass_len}')
        return
    possible_elements = ascii_letters + digits + '*-+/><.,'
    password = choices(possible_elements, k=pass_len)
    return ''.join(password)


print(generate_password(50))