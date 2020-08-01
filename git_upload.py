import os

os.system('git add .')
message = input("Enter git commit message: ")
os.system('git commit -m "{}"'.format(message))
os.system('git push')