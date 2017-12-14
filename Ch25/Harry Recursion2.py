def groupSum(start,array,target):
    if target == 0:
        return True
    elif start == len(array):
        return False
    return groupSum(start+1,array,target = target-array[start] or groupSum(start,array,target))

def groupSum6(start,array,target):
    if start == len(array):
        return target == 0
    elif array[start] == 6:
        return groupSum6(start+1,array,target-array[start])
    else:
        return groupSum6(start+1,array,target-array[start]) or groupSum6(start+1,array,target)

def groupNoAdj(start,array,target):
    if start == len(array):
        return target == 0
    return groupNoAdj(start+2,array,target-array[start]) or groupNoAdj(start+1,array,target)

def groupSum5(start,array,target):
    if start == len(array):
        return target == 0
    if array[start] % 5 == 0:
        if start < len(array)-1 and array[start+1] == 1:
            return groupSum5(start+2,array,target-array[start])
        return groupSum5(start+1,array,target-array[start])
    return groupSum5(start+1,array,target-array[start]) or groupSum5(start+1,array,target)

def groupSumClump(start,array,target):
    if start+1 > len(array):
        return target == 0
    elif start < len(array)-1:
        if array[start] == array[start+1]:
            i = start
            while i < len(array)-1 and array[i] == array[i+1]:
                i += 1
            i += 1
            return groupSumClump(i,array,target) or groupSumClump(i,array,target-(i-start)*array[i-start])
    return groupSumClump(start+1,array,target) or groupSumClump(start+1,array,target-array[start])
