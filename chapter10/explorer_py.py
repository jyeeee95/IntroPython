import os
import time
from itertools import chain
from collections import defaultdict



def search(OrgDir, Depthkey):
    key = Depthkey

    ab_OrgDir = os.path.abspath(OrgDir)
    files = os.listdir(ab_OrgDir)


    for file in files:
        ab_file = ab_OrgDir + "/" + file

        if os.path.isfile(ab_file):
            FileList.append({key: ab_file})

        elif os.path.isdir(ab_file):

            SubDir = ab_file
            DirList.append({key: ab_file})

            search(SubDir, Depthkey + 1)
        else:
            print("else")



# 시작 시간 받기
start_time = time.time()

dir = "/Users/jyeeee95/IntroPython" #os.getcwd()
FileDict = dict()
DirDict = dict()

FileList = []
DirList = []

DepthKey = 1
search(dir, 1)


ForFilePrint = defaultdict(list)
ForDirPrint = defaultdict(list)

# 파일 출력
print("\n---------------------------file list\n")
for i in range(0, len(FileList)-1):
    for k, v in chain(FileList[i].items(), FileList[i+1].items()):
        ForFilePrint[k].append(v)

for k, v in ForFilePrint.items():
    print(k)
    for i in v:
        print(i)



# 디렉토리 출력
print("\n---------------------------directory list\n")
for i in range(0, len(DirList)-1):
    for k, v in chain(DirList[i].items(), DirList[i+1].items()):
        ForDirPrint[k].append(v)

for k, v in ForDirPrint.items():
    print(k)
    for i in v:
        print(i)


# 걸린 시간 반환
print("\n---------------------------코드 수행 시간: " + str(time.time() - start_time))
