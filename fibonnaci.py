#Fibonnaci Seies with in a particular range

def fib(start,end):
    a=0
    b=1
    while a<=end:
        if a>=start:
            print(a,end=' ')
        a,b=b,a+b
try:
    start=int(input("Enter Start Range Number : "))
    end=int(input("Enter End Range Number : "))
    if start<0 or end<0:
        print("enter positive int")
    elif start>end:
        print("Invalid")
    else:
        print("Start and End Range is : ",[start,end])
        fib(start,end)
except ValueError:
    print("Invalid Input")