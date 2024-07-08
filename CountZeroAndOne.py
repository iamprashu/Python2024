def Counter(arr,size):
    zero = 0
    one = 0

    for i in range(size):
        if(arr[i]==0):
            zero+=1
        elif(arr[i]==1):
            one+=1
    
    return (zero,one) 


arr = [1,2,3,0,0,1,0,0,0,10,10,10,10,10,1,1,1,1,10,0,0,10,10,0,0,0,0,]

size = len(arr)

answer = Counter(arr,size)

zero = answer[0]

one = answer[1]

print(f"Zeros are : {zero} and ones are : {one}")