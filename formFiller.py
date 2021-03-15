#!python3
'''
    formFiller.py - preenchimento automático do formulário
'''
import pyautogui, time

# Defina essas variáveis com as coordenadas corretas obtidas em seu computador
nameField = (770, 369)
submitButton = (691, 975)
submitButtonColor = (130, 130, 130)
submitAnotherLink = (816, 260)

formData = [
    {'name': 'Alice', 'fear': 'cavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I sad hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a.'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]
pyautogui.PAUSE = 0.5

for person in formData:
    # Oferece ao usuário uma chance de encerrar o script
    print('>>>> 5 SECONDS PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    # Espera até que a página do formulário tenha sido carregada
    # while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
    #     time.sleep(0.5)
    print(f'Entering {person["name"]}...')
    pyautogui.click(nameField[0], nameField[1])

    # Preenche o campo Name
    pyautogui.typewrite(person['name'] + '\t')
    # Preenche o campo Greatest Fear(s)
    pyautogui.typewrite(person['fear'] + '\t')
    # Preenche o campo Source of Wizard Powers
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])
    # Preenche o campo RoboCop
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])
    # Preenche o campo Additional Comments
    pyautogui.typewrite(person['comments'] + '\t')
    # Clica em Submit
    pyautogui.press('enter')
    # Espera até que a página do formulário tenha sido carregada
    print('Clicked Submit.')
    time.sleep(5)
    # Clica no link Submit Another Response
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
