#Sum of all odd natural Numbers

try:
    n=int(input("Enter a Number : "))
    if n<=0:
        print("Enter positive integer")
    else:
        total=0
        for i in range(1,n+1,2):
            total+=i
        print(total)
except ValueError:
    print("Invalid Input")