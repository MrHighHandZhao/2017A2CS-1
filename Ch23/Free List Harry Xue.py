#Free list Example
#Harry Xue Opt 3


NextP = -1

class FreeList:
    def __init__(self):
        self.Value = ""
        self.Next = NextP

def InitializeList():
    List = [FreeList() for i in range(10)]
    StartP = NextP
    FreeLP = 0
    for i in range(9):
        List[i].Next = i + 1
    List[9].Next = NextP
    print(List)
    print(StartP,FreeLP)
            
InitializeList()
