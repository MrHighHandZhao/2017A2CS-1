def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist =[]
num = int(input("how many number are in the array \n"))
count = 0
while count < num:
    a = int(input("please input an array \n"))
    alist.append(a)
    count = count+1
bubbleSort(alist)
print(alist)
