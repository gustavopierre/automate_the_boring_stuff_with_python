#!python3
passwords = {'email': 'F7mr23Tre6xyABC8B9', 'blog': 'Vmx876ReTeBB123', 'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py {account] - copy acount passaword')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)