import wget
import os
import sys

user_input = input("Enter file path: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

#raam = os.getcwd()
#print(raam)

raam = open(user_input, 'r')
url = raam.readlines()
print(url)

for line in url:
    wget.download(line.rstrip())

print("Download completed successfully - Python")
