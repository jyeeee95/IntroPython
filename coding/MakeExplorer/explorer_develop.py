import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
import time
from itertools import chain
from collections import defaultdict




class SetInput():
    def __init__(self):
        self.SearchSpot = ""
        self.SaveSpot = ""

    def GetAddress(self):
        self.SearchSpot = input("탐색할 위치를 입력하세요 : ")
        self.SaveSpot = input("탐색 결과를 저장할 위치를 입력하세요: ")

        return self.SearchSpot, self.SaveSpot

    def ErrorCheck(self, setlist):

        return myFunction




class WriteFile():
    def __init__(self, SaveSpot):
        self.Address = SaveSpot + "/SearchResult.txt"
        self.MyFile = open(self.Address, "w")



    def ForWrite(self, SaveSpot, MyList):

        ListForPrint = defaultdict(list)

        # 파일 출력
        for i in range(0, len(MyList)-1):
            for k, v in chain(MyList[i].items(), MyList[i+1].items()):
                ListForPrint[k].append(v)

        for depth, files in ListForPrint.items():
            for file in files:
                self.MyFile.write(file + "\n")







if __name__ == "__main__":

    start_time = time.time()

    def Search(SearchSpot, Depthkey):
        # get abspath
        Address = os.path.abspath(SearchSpot)
        # For Checking Depth
        key = Depthkey

        # search abspath
        Searching = os.listdir(Address)

        for File in Searching:
            Abs = Address + "/" + File

            if os.path.isfile(Abs):
                FileList.append({key: Abs})

            elif os.path.isdir(Abs):
                DirList.append({key: Abs})

                # 재귀
                Search(Abs, key + 1)

            else:
                print("error" + Abs)



    Setting = SetInput()
    SearchSpot, SaveSpot = Setting.GetAddress()

    # setting list
    FileList = []
    DirList = []

    Search(SearchSpot, 1)


    WriteFile = WriteFile(SaveSpot)
    MyFile = WriteFile.MyFile

    MyFile.write("수행 시간 :::\n")
    MyFile.write(str(time.time() - start_time))

    MyFile.write("\n\nFileList :::\n")
    WriteFile.ForWrite(SaveSpot, FileList)

    MyFile.write("\n\nDirList :::\n")
    WriteFile.ForWrite(SaveSpot, DirList)

    MyFile.close()












    #
