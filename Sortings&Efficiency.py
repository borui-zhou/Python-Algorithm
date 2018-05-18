# Sorting Algorithms
# Comparing the efficiency/speed of selection, bubble, and insertion sorts

import time
import random

# Selection Sort
def selSort(x):
    for j in range( len(x) - 1 ):
        index = j
        for i in range( j+1,len(x) ):
            if x[i] < x[index]:
                # The new element to the right is less than
                # the current smallest element, so reset the
                # position of the smallest element
                index = i
        if index != j:
            # After passing through the list, the index has
            # of the smallest element has changed -> swap elements
            swap = x[j]
            x[j] = x[index]
            x[index]=swap
        #print(x)            # Output the result of each pass

# Bubble Sort
def bubSort(x):
    for j in range(1, len(x)-1):
        for i in range( len(x) - j):
            if x[i] > x[i+1]:
                # The current element is larger than the element to
                # the right -> swap elements
                swap = x[i]
                x[i] = x[i+1]
                x[i+1] = swap
                 # Indicates that a swap has occurred
        #print(x)                 # Output the result of each pass
            # As soon as the list is passed through and no swap has
            # occurred, the list must be sorted

    
# Insertion Sort
def insertSort(x):
    for i in range(1,len(x)):
        valueToInsert = x[i]
        holePos = i
        while holePos > 0 and valueToInsert < x[holePos-1]:
            # value to insert does not belong where the hole
            # currently is, so shift
            a[holePos] = a[holePos-1] # shift larger value up
            holePos = holePos - 1     # move hole position down
        # hole is in proper position -> put valueToInsert into the hole
        a[holePos] = valueToInsert
        # a[0..i] is now in sorted order
        
        #print(a)            # Output the result of each pass

# Sorting Algorithm Timing (START HERE! - SORTING ASSIGNMENT)

# Set up the array to be sorted
def reada(a,num):
    f=open("number.txt","r")
    n=num
    a=[]
    for i in range(n):
        k=0
        x=1
        new=f.read(1)
        if new=="-":
            x=-1
            new=f.read(1)
        while new!=",":
            k=k*10+int(new)
            new=f.read(1)
        a.append(k*x)
    f.close()
    return a


#print(a)

# Timing the Sort
n=[]
for i in range(100,1000,100):
    n.append(i)
for i in range(1000,10000,1000):
    n.append(i)
for i in range(10000,100000,10000):
    n.append(i)
tinsert=[]
tbub=[]
tselc=[]
addd=5
lenth=len(n)-addd
for i in range(lenth):
    a=[]
    a=reada(a,n[i])
    start_time = time.time()
    selSort(a)                 
    stop_time = time.time()
    time_msecs = int((stop_time-start_time)*1000)
    tselc.append(time_msecs)
for i in range(lenth):
    a=[]
    a=reada(a,n[i])
    start_time = time.time()
    bubSort(a)                 
    stop_time = time.time()
    time_msecs = int((stop_time-start_time)*1000)
    tbub.append(time_msecs)
for i in range(lenth):
    a=[]
    a=reada(a,n[i])
    start_time = time.time()
    insertSort(a)                 
    stop_time = time.time()
    time_msecs = int((stop_time-start_time)*1000)
    tinsert.append(time_msecs)
f=open("CMPresult.txt","w")
for i in range(lenth):
    w_n=str(n[i])
    f.write(w_n)
    f.write(",")
for i in range(lenth):
    c_t=str(tselc[i])
    f.write(c_t)
    f.write(",")
for i in range(lenth):
    c_t=str(tbub[i])
    f.write(c_t)
    f.write(",")
for i in range(lenth):
    c_t=str(tinsert[i])
    f.write(c_t)
    f.write(",")
f.close()


