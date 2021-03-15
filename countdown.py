#!python3
'''
    countdown.py - um script simples para contagem regressiva
'''
import time, subprocess

timeLeft = 40
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)
