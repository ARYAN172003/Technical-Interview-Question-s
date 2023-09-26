# inverted pyramid

def pyramid(rows):
    for i in range(rows,0,-1):
        for j in range(rows-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()
try:
    rows=int(input("Enter Number : "))
    if rows<=0:
        print("please enter a positive integer")
    else:
        pyramid(rows)
except ValueError:
    print("Invalid Input")