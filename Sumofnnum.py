# Sum of all n natural no.s

try:
    n=int(input("Enter a Number : "))
    if n<=0:
        print("Enter the positive number")
    else:
        total=0
        for i in range(1,n+1):
            total+=i
        print(total)
except ValueError:
    print("Invalid Input")