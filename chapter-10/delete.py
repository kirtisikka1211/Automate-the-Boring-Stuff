import os
import shutil
folder="/Users/kirtisikka/Documents/python/chapter10"
# =input("The size u want to ignore")
for folders, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        file_user = os.path.getsize(os.path.join(folders, filename))
        
        if file_user > 104857600:   
            print(filename, '| Size = ', file_user // 104857600, 'MB' '| Path =',
                  os.path.join(folders, filename))
    # print(os.path.abspath(filename))