import os, sys
from zipfile import ZipFile

#raam = os.getcwd()

input_file_path = input("Enter folder path: ")

if len(sys.argv) < 1:
    raam = input_file_path = sys.argv[1]
else:
    raam = os.getcwd()    

for file in raam:
    def unzip (path, total_count):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_name = os.path.join(root, file)
                if (not file_name.endswith('.zip')):
                    total_count += 1
                else:
                    currentdir = file_name[:-4]
                    if not os.path.exists(currentdir):
                        os.makedirs(currentdir)
                    with ZipFile(file_name) as zipObj:
                        zipObj.extractall(currentdir)
                    os.remove(file_name)
                    total_count = unzip(currentdir, total_count)
        return total_count

total_count = unzip ('.', 0)
#print(total_count)
print("Unzipped files in the folder")
