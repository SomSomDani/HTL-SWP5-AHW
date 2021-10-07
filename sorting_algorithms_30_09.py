import copy
import random;
def bubblesort(mlist):
    n = len(mlist)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mlist[j] > mlist[j + 1]:
                mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]
    return mlist
def insertionsort(mlist):
    for i in range(1, len(mlist)):
        key = mlist[i]
        j = i - 1
        while j >= 0 and key < mlist[j]:
            mlist[j + 1] = mlist[j]
            j -= 1
        mlist[j + 1] = key
    return mlist
def selectionsort(mlist):
    for i in range(len(mlist)):
        min_idx = i
        for j in range(i + 1, len(mlist)):
            if mlist[min_idx] > mlist[j]:
                min_idx = j
        mlist[i], mlist[min_idx] = mlist[min_idx], mlist[i]
    return mlist

if __name__ == "__main__":
        nlist = []
        nlist2 = []
        nlist3 = []
        for j in range(0, 100):
            n = random.randint(0,100)
            nlist.append(n)
        nlist2, nlist3 = copy.deepcopy(nlist), copy.deepcopy(nlist)
        bsortlist = bubblesort(nlist)
        isortlist = insertionsort(nlist2)
        ssortlist = selectionsort(nlist3)
        print(bsortlist)
        print(isortlist)
        print(ssortlist)
