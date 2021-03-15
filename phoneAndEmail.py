#!python3

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # código de área
    (\s|-|\.)?                      # separador
    (\d{3})                         # três primeiros dígitos
    (\s|-|\.)                       # separador
    (\d{4})                         # quatro últimos dígitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extensão
)''', re.VERBOSE)
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # nome do usuário
    @                   # símbolo @
    [a-zA-Z0-9.-]+      # nome do domínio
    (\.[a-zA-Z]{2-4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNumb = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNumb += 'x' + groups[8]
    matches.append(phoneNumb)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')