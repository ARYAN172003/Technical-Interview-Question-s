#Right Sided * pyramid

def pyramid(rows):
    for i in range(1,rows+1):
        for j in range(rows-i):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()
try:
    rows=int(input("Enter a Numbeer : "))
    if rows<0:
        print("Enter positive integer")
    else:
        pyramid(rows)
except ValueError:
    print("Invalid Input")