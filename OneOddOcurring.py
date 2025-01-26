def oneoddaccur(arr):
    res=0
    for element in arr:
        res = res^element
    return res

arr=[]
n=int(input("Enter the array size: "))
while(n):
    num=int(input("Enter value: "))
    arr.append(num)
    n-=1

print("The One Odd Ocurring value is: ",oneoddaccur(arr))