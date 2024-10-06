#1 algolithm

def algorithm1(arr, num):
    for i in range(len(arr)):
        if arr[i] + arr[i+1] == num:
            return True
        else:
            return False

print(algorithm1([1,4,5,6], 9)) 

#2 algorithm


