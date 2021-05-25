import os, sys

#rootdir = os.getcwd()

input_file_path = input("Enter folder path: ")

if len(sys.argv) < 1:
    rootdir = input_file_path = sys.argv[1]
else:
    rootdir = os.getcwd()   

for subdir, dirs, files in os.walk(rootdir):
    for filename in files:
        if filename.endswith(('Manuscript_v1.DOCX', 'Manuscript_v1.DOC')):
            filepath = subdir + os.sep + filename
            filepath1 = filepath.rstrip()
            #print(filepath1)
            for path, dirs, files in os.walk(rootdir):
                if len(dirs) == 0:
                    raam1 = os.path.basename(subdir)
                    #print(raam1)
                    raam2 = raam1.split("-")[3:]
                    raam3 = ''.join(map(str, raam2))
                    raam = raam3.replace(".", "-")
                    #print(raam)
                    dirname = os.path.dirname(filepath1)
                    newpath = dirname + os.sep + raam + '.DOCX'
                    #print(newpath)
            os.rename(filepath1, newpath)
print('Successfully renamed files - PyThOn')



