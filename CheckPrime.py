number = input("Please Enter Number Here :> ")
number = int(number)

if(number==1 or number==0):
    print("Not Prime")
elif(number==2):
    print("Yess it is Prime !")

for i in range(2,number):
    if(number%i==0):
        print("Not a Prime !")
        break
    else:
        print("Yes It is Prime !!!!!!!!!")
        break