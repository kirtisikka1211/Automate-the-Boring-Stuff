import re
import os
user_input = input("Enter your expression: ")


folder = os.listdir()
print(folder)
try:
    for user_file in folder:
        if user_file.endswith('.txt'): 
            open_file = open(user_file,'r')
            read_file = open_file.read()
            open_file.close()
            y=read_file.find(user_input)
            if y==-1:
                print("The expression dosnt exist in ",user_file)
            else:
                print("The expression exist in ",user_file)
           
except:
    print("Doesnt exist")
