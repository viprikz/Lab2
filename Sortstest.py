#import unittest   # The test framework
class QuickSort(object):
    low = 0
    high = 0
    arr = [ ]
    def __init__(self, arr):
        self.arr = arr
        self.high = (len(arr) - 1)
    def partition(self, low, high):
        """Moving elements 
        
        Arguments:
            low {[int]} -- low index
            high {[int]} -- high index
        
        Returns:
            [int] -- index
        """
        i = ( low-1 )
        pivot = self.arr[high]
        for j in range(low , high): 
             if   self.arr[j] <= pivot: 
                i = i+1 
                self.arr[i],self.arr[j] = self.arr[j],self.arr[i] 
        self.arr[i+1],self.arr[high] = self.arr[high],self.arr[i+1] 
        return ( i+1 ) 

    def quickSort(self, low, high): 
        """Sorting
        
        Arguments:
            low {int} -- index
            high {int} -- index
        """
        if  low <  high: 
            pi =  self.partition(low,high) 
            self.quickSort(low, pi-1) 
            self.quickSort(pi+1, high)

    def start(self):
        if(not self.Check()):
            self.quickSort(self.low, self.high)
            return self.arr
        else:
            return ("wrong array")

    def reverse(self):
        bufarr = self.arr
        for i in range (0, len(bufarr)):
            self.arr[i] = bufarr[len(bufarr) - i]

    def CountBigO(self):
        return("n * n")

    def Check(self):
        flag = False
        for i in range(len(self.arr)):
            if(not type(self.arr[i]) is int):
                flag = True
                print(flag)
                print(self.arr[i])
        return flag




class MergeSort(object) :
    arr = []
    def __init__(self, array):
        self.arr = array
    def merge(self,l, m, r) :
        """merging subarrays
        
        Arguments:
            l {int} -- left index
            m {int} -- midl index
            r {int} -- right index
        """
        n1 = m - l + 1
        n2 = r- m 
        L = [0] * (n1) 
        R = [0] * (n2) 
        for i in range(0 , n1): 
            L[i] = self.arr[l + i] 
        for j in range(0 , n2): 
            R[j] = self.arr[m + 1 + j] 
        i = 0  
        j = 0 
        k = l 
        while i < n1 and j < n2 : 
            if L[i] <= R[j]: 
                self.arr[k] = L[i] 
                i +=1
            else: 
                self.arr[k] = R[j] 
                j += 1
            k += 1
        while i < n1: 
            self.arr[k] = L[i] 
            i += 1
            k += 1
        while j < n2: 
            self.arr[k] = R[j] 
            j += 1
            k += 1

    def mergeSort(self,l,r): 
        """List moving
        
        Arguments: 
            l {[int]} -- left index
            r {[int]} -- right index
        """
        if l < r:
            m = (l+(r-1))//2
            self.mergeSort(l, m) 
            self.mergeSort(m+1, r) 
            self.merge(l, m, r) 

    def start(self):
        """ 
    Merges two subarrays of arr[]. 
    First subarray is arr[l..m] 
    Second subarray is arr[m+1..r] 
    
    Returns:
        [list] -- array
    """
        if(self.Check):
            self.mergeSort(0,len(self.arr) - 1)
            return self.arr
        else:
            print("wrong array")

    def reverse(self):
        """reverse list 
        """
        bufarr = self.arr
        for i in range (0, len(bufarr)):
            self.arr[i] = bufarr[len(bufarr) - i]

    def CountBigO(self):
        return("n * log2(n)")
    
    def Check(self):
        """checking data
        
        Returns:
            boolean -- error flag
        """
        flag = False
        for i in range(len(self.arr)):
            if(not str.isdigit(arr[i])):
                flag = True
        return flag

class RadixSort(object):
    arr = []
    def __init__(self, array):
        self.arr = array
    def radixSort(self): 
        """exponent changing
        """
        max1 = max(self.arr) 
        exp = 1
        while max1/exp > 0: 
            self.countingSort(exp) 
            exp *= 10

    def countingSort(self, exp1): 
        """sorting by 1 number
        
        Arguments:
            exp1 {int} -- exponent
        """
        n = len(self.arr) 
        output = [0] * (n) 
        count = [0] * (10) 
        for i in range(0, n): 
            index = (self.arr[i]//exp1) 
            #print("index is")
           # print(index)
            count[ (index)%10 ] += 1
        for i in range(1,10): 
            count[i] += count[i-1] 
        i = n-1
        while i>=0: 
            index = (self.arr[i]//exp1) 
            output[ count[ (index)%10 ] - 1] = self.arr[i] 
            count[ (index)%10 ] -= 1
            i -= 1
        i = 0
        for i in range(0,len(self.arr)): 
            self.arr[i] = output[i] 
    def start(self):
        if(self.Check):
            self.radixSort()
            return self.arr
        else:
            print("wrong array")

    def reverse(self):
        """reverse array
        """
        bufarr = self.arr
        for i in range (0, len(bufarr)):
            self.arr[i] = bufarr[len(bufarr) - i]

    def CountBigO(self):
        return("n")
    def Check(self):
        flag = False
        for i in range(len(self.arr)):
            if(not str.isdigit(arr[i])):
                flag = True
        return flag


array = [14,554,134,653,234,4,2,34,5,90] 
n = len(array) 
arr = QuickSort(array).start()
#arr = MergeSort(array).start().reverse()
#arr = QuickSort(array).start().reverse()
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])