import os, sys

#rootdir = os.getcwd()

input_file_path = input("Enter folder path: ")

if len(sys.argv) < 1:
    rootdir = input_file_path = sys.argv[1]
else:
    rootdir = os.getcwd()    

for subdir, dirs, files in os.walk(rootdir):
    for filename in files:
        if filename.endswith('.xml'):
            filepath = subdir + os.sep + filename
            filepath1 = filepath.rstrip()
            #print(filepath1)
            for path, dirs, files in os.walk(rootdir):
                if len(dirs) == 0:
                    raam4 = os.path.basename(subdir)
                    raam5 = raam4.replace("_internal_v2.zip", "_meta.xml")
                    #print(raam5)
                    dirname = os.path.dirname(filepath1)
                    newpath = dirname + os.sep + raam5
                    #print(newpath)
            os.rename(filepath1, newpath)
print("meta file renamed sucessfully - pYtHoN")
