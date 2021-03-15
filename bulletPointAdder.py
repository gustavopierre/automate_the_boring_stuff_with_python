#!python3
import pyperclip

text = pyperclip.paste()
pyperclip.copy(text)
# print(text +'\n\n\n')
lines = text.split('\n')
for count in range(len(lines)):
    lines[count] = '* ' + lines[count]
    #print(lines[count])

# print(lines)
# print('\n\n\n' + text +'\n\n\n')
text = '\n'.join(lines)

pyperclip.copy(text)
