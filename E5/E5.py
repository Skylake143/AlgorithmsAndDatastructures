import numpy as np
import copy
#Reorder negative and positive values
def question1():
    A = [-1,4,-6,4,5,3,-4,5]
    i = 0
    j = len(A)-1
    while(i<=j):
        if A[i] < 0:
            i+=1
        else: 
            #Swap elements
            swap = A[i]
            A[i] = A[j]
            A[j] = swap
            j-=1
        
    return A

#Dutch flag problem
#All below r index is red
#All in between r and w index is white and all above b index is blue
def question2():
    A=['R','W','B','W','W','R','B','B','R','W','W','B','R']
    r = 0
    w = 0
    b = len(A)-1
    while(w<=b):
        if A[w] == 'R':
            swap = A[w]
            A[w] = A[r]
            A[r] = swap
            r+=1
            w+=1
        else: 
            if A[w] == 'W': 
                w+=1
            else:
                swap = A[w]
                A[w] = A[b]
                A[b] = swap
                #Swap elements
                b-=1
                
    return A

#Question 3 Find smallest element in array
#1. Split up list and compare each entry of the two arrays with the other array
#2. Merge arrays again by using the minimum of the two elements
def recursive_comparison(A):
    if len(A)==1: return A[0]
    A1 = A[0:int(len(A)/2)]
    A2 = A[int(len(A)/2):len(A)]

    newA = np.zeros(int(len(A)/2))

    for i in range(len(A1)):
        if A1[i] <= A2[i]:newA[i] = A1[i]
        else: newA[i] = A2[i]
    return recursive_comparison(newA)
      
    
def question3():
    A = [3,7,4,3,6,8,3]
    if len(A)%2==1: 
        A = [float(entry) for entry in A]
        A.append(np.inf)
    return int(recursive_comparison(A))
    
def question5BruteForce():
    A=[3,-1,4,-8,2,-4]
    counter = 0
    i=0
    while i < len(A):
        j=1
        while j<len(A):
            if A[i] + A[j] == 0: counter += 1
            j+=2 
        i+=2
    return counter


def amount2(A,left, right):
    counter = 0
    #Also possible to do it the other way around and check if right = left + 2
    if (right - left)>2:
        counter += amount2(A, int(left),int((right-left)/2))
        counter += amount2(A, int(left+(right-left)/2),int(right))
        return counter

    j=1
    while j<len(A):
        if A[left] + A[j] == 0: 
            counter += 1
        j+=2 
    return counter

def question5DivideAndConquer():
    A=[3,-1,4,-8,2,-4,5,-10,10,-5,3,-24,7,-34,32,-345]
    return amount2(A, 0,len(A))

#Question 7 closest pair
def closest_pair(arr,left, right):
    if right==left:
        return np.inf
    
    mid = int((left+right)/2)
    ld = closest_pair(arr,left,mid)
    rd = closest_pair(arr,mid+1,right)
    md = arr[mid+1]-arr[mid]
    return np.min([ld, rd, md]) 

def question7closestPair():
    arr = [1.0,4.3,6.5,4.7,5.4,3.3,3.2,4.4,5.1]
    sortarr = sorted(arr)
    return closest_pair(sortarr, 0,len(sortarr)-1)

def quesiton7nonrecursive():
    arr = [1.0,4.3,6.5,4.7,5.4,3.3,3.2,4.4,5.1]
    sortarr = sorted(arr)
    minimum = sortarr[1]-sortarr[0]
    for i in range(2,len(sortarr)):
        tempdistance = sortarr[i]-sortarr[i-1]
        if  tempdistance < minimum:
            minimum = tempdistance
    return minimum
        




if __name__ == "__main__":
    print("Question 1: Order negative/positive of array [-1,4,-6,4,5,3,-4,5]: ",question1())
    print("Question 2: Dutch flag problem of array ['R','W','B','W','W','R','B','B','R','W','W','B','R']", question2())
    print("Question 3: Smallest element: ", question3())
    print("Question 5: Number of pairs Brute Force: ", question5BruteForce())
    print("Question 5: Number of pairs DaC: ", question5DivideAndConquer())
    print("Question 7: DivideAndConquer Closest Pair: ", question7closestPair())
    print("Question 7: Non Recursive closest pair: ", question7closestPair())




