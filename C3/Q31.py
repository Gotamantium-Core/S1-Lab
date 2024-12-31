'''
Use divide and conquer to find the element that appears most frequently
in an array. Divide the array into two halves, find the most frequent
element in each half, and combine these results to determine the overall
most frequent element.
'''

def count(arr, element, left, right):
    count = 1
    for i in arr[left: right+1]:
        if i == element:
            count += 1

    return count


def Freq(arr):
    def freqUtil(arr, left, right):
        if left == right:
            return arr[left]

        mid = (left + right)//2

        L = freqUtil(arr, left, mid)
        R = freqUtil(arr, mid+1, right)

        if L == R:
            return L
        
        Lcount = count(arr, L, left, right)
        Rcount = count(arr, R, left, right)
    
        return L if Lcount > Rcount else R
    
    return freqUtil(arr, 0, len(arr)-1)

arr = [1, 1, 2, 2, 2, 2, 3, 4]

print(Freq(arr))