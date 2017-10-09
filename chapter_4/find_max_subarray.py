def crossingsubarray(A, low, mid, high):
    negativeinfinity = -10000000000
    leftsum = 0
    for i in range(mid, low - 1, -1):
        leftsum = leftsum + A[i]
        if leftsum > negativeinfinity:
            negativeinfinity = leftsum
            leftindex = i
    left = negativeinfinity


    negativeinfinity = -10000000000
    rightsum = 0

    for j in range(mid+1, high+1):
        rightsum = rightsum + A[j]
        if rightsum > negativeinfinity:
            negativeinfinity = rightsum
            rightindex = j
    right = negativeinfinity

    return(leftindex, rightindex, left + right)

def findmaxarray(alist, low, high):

    if high == low:
        return low, high, alist[low]

    else:
        mid = (low+high)/2

        leftlow, lefthigh, leftsum = findmaxarray(alist, low, mid)
        rightlow, righthigh, rightsum = findmaxarray(alist, mid + 1, high)
        crosslow, crosshigh, crosssum = crossingsubarray(alist, low, mid, high)

        print leftlow, lefthigh, leftsum, "leftlow, lefthigh, leftsum"
        print rightlow, righthigh, rightsum, "rightlow, righthigh, rightsum"
        print crosslow, crosshigh, crosssum, "crosslow, crosshigh, crosssum"

        if leftsum >= rightsum and leftsum >= crosssum:   
            return leftlow, lefthigh, leftsum

        elif rightsum >= leftsum and rightsum >= crosssum:    
            return rightlow, righthigh, rightsum

        else:    
            return crosslow, crosshigh, crosssum

B = [-7, -2, 5, 4, -1, 100, 10]

L,H,maxi = findmaxarray(B, 0, 6)



print(L)
print(H)
print(maxi)