

def DutacNationalFlag(arr,size):
   start = 0
   mid=0
   end = size-1

   while(mid<=end):
      
      match arr[mid]:
         
        case 0 : 
            temp = arr[mid]
            arr[mid] = arr[start]
            arr[start] = temp
            start +=1
            mid +=1
        case 1 : 
            mid += 1
        case 2 : 
            temp = arr[mid]
            arr[mid]=arr[end]
            arr[end] = temp
            end -=1
         



arr = [1,2,1,2,0,1,2,0,1,2,0,0,0,0,1,0,2,1]
size = len(arr)

DutacNationalFlag(arr,size)

for i in range(len(arr)):
   print(f"|{ arr[i] }|", end= " ")