#! python3
# pw.py - An insecure password locker program.

import sys, pyperclip, string, random

PASSWORDS = {'email': 'yz6B3A0i7JtyMU6',
             'blog': '1smXkBH9y01MNLo',
             'luggage': '3SI2krgawTuI4Ny'}

def pass_generator(size = 15, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    PASSWORDS[account] = pass_generator()
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' created and copied to clipboard.')

print (PASSWORDS) # to check that it works