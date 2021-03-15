#!python3
import re, pyperclip


def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(text)
    return mo.group()


print('Usaremos o texto que está no clipboad.')

text = pyperclip.paste()

phoneNumber = isPhoneNumber(text)
if phoneNumber == None:
    print('Não foi achado nenhum número!') 
else:
    print('Phone number found: ' + phoneNumber)
    