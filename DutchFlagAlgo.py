arr = [0,0,0,0,1,1,2,1,2,1,1,0,1,0,1,2]
# i need to get count of each element and sort the array

# i am using dutch national flag

zero = 0
one = 0
two = 0
# There are to store count

start = 0 
mid = 0
end = len(arr)-1

while(mid<=end):

    match(arr[mid]):

        case 0 :
            zero +=1
            temp = arr[mid]
            arr[mid] = arr[start]
            arr[start] = temp
            #this is to swap the elements
            start+=1
            mid +=1
        case 1:
            one+=1
            mid += 1
        case 2:
            two+=1
            temp = arr[mid]
            arr[mid] = arr[end]
            arr[end] = temp
            end -=1

# at last after sorting geeting count printed

print(f"Here is the count of elements :\n Count of zero is :{zero} \n Count of One is : {one} \n Count of Two is : {two} .")

print(arr)