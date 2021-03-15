#!python3
import threading, time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Weak up')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')