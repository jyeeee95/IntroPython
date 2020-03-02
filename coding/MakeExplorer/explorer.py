import os
import time



def search(OrgDir, key):
    DepthKey = key
    ab_OrgDir = os.path.abspath(OrgDir)
    files = os.listdir(ab_OrgDir)
    # print(files)

    FileList = []
    DirList = []

    for file in files:

        ab_file = ab_OrgDir + "/" + file

        if os.path.isfile(ab_file):
            FileList.append(ab_file)
            newFileDict = {DepthKey: FileList}
            temp1.append(newFileDict)

        elif os.path.isdir(ab_file):
            DirList.append(ab_file)

            SubDir = ab_file
            search(SubDir, DepthKey + 1)

        else:
            print("else")

        print(DepthKey)
        newDirDict = {DepthKey: DirList}
        temp2.append(newDirDict)




# 시작 시간 받기
start_time = time.time()

dir = "/Users/jyeeee95/IntroPython" #os.getcwd()
FileDict = dict()
DirDict = dict()

temp1 = []
temp2 = []

DepthKey = 1
search(dir, 1)

print(temp1)

print(time.time() - start_time)
