import os, sys
import shutil

#raam = os.getcwd()

input_file_path = input("Enter folder path: ")

if len(sys.argv) < 1:
    raam = input_file_path = sys.argv[1]
else:
    raam = os.getcwd()    
contents = os.listdir(raam)

for items in contents:
     if os.path.isdir(items):
         filename = items + os.sep + 'Bookin'
         #print(filename)
         os.makedirs(filename)
         walker = os.walk(items)
         rem_dirs = walker.__next__()[1]
         for data in walker:
             for files in data[2]:
                 try:
                      shutil.move(data[0] + os.sep + files, filename)
                 except shutil.Error:
                      continue
print("Files moved to Bookin Folder")

   
