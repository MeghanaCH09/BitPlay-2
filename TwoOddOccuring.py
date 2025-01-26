def twooddnums(arr,size):
    xorof2=arr[0]
    x=0
    y=0
    sebit=0
    for i in range(1,size):
        xorof2= xorof2^arr[i]
    setbit=xorof2 & ~ (xorof2-1)

    for i in range(size):
        if (arr[i]&setbit):
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("Two Odd Occuring Values are", x, "&", y)

arr=[]
arr_size=int(input("Enter the array size: "))
for i in range(0,arr_size):
    z=int(input("Enter a value: "))
    arr.append(z)

twooddnums(arr, arr_size)