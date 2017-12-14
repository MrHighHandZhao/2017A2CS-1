#Harry Xue

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
def BinarySearch(alist,value):
    value = int(input("Which value do you want? \n"))
    low = 0
    high = len(alist)-1
    while found == False and searchfailed == False:
        mid = int((high+low)/2)
        if alist[mid] == value:
            found = True
        else:
            if low >= high:
                searchfailed = True
            else:
                if alist[mid] > value:
                    high = int(mid-1)
                else:
                    low = int(mid+1)
    if found == True:
        print("The position is"+str(low))
    else:
        print("Item not found!")

alist =[]
num = int(input("How many number are in the array \n"))
count = 0
while count < num:
    a = int(input("Please input an array \n"))
    alist.append(a)
    count = count+1
bubbleSort(alist)
BinarySearch(alist)
print(alist)


    
