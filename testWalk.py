import os

for folderName, subFolders, filenames in os.walk('D:\\temp'):
    print('The current folder is ' + folderName)
    for subFolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subFolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')
