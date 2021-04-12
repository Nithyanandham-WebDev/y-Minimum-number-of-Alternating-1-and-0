

# /I want to find the minimum number of flips required to get an alternating of [0, 1, 0, 1]
# for example given [1, 1, 0, 1]. so in this case, it is one flip

def solution(A):
    count = 0
    myDict = {}
    myDict[1] = True
    myDict[0] = False

    next = None
    find_value = myDict[A[0]]
    if find_value == True:
        next = False
    else:
        next = True

    for element in A[1:]:
        if next != myDict[element]:
            count += 1
            myDict[element] = next
        if myDict[element] == True:
            next = False
        else:
            next = True

    return count

print(solution([1,1,0,1]))