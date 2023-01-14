import os
import shutil
folder = "/Users/kirtisikka/Documents/python/chapter10"
extension = input("Enter the extension you'd like to copy: ")
destination = "/Users/kirtisikka/Documents/python/chapter101"
for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:

            if filename.endswith('{}'.format(extension)):
                shutil.copy(os.path.join(folders, filename), destination)

print('Selective copying has finished - all files of', extension,
      'type have been copied from', os.path.basename(folder), 'to',
      os.path.basename(destination))