# Sum of all even natural numbers

try:
    n=int(input("Enter a Number : "))
    if n<0:
        print("Enter positive integer")
    else:
        total=0
        for i in range(2,n+1,2):
            total+=i
        print(total)
except ValueError:
    print("Invalid Input")