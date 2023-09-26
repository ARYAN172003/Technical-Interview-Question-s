def pyramid(rows):
    for i in range(rows,0,-1):
        for j in range(i):
            print("*",end="")
        print()
try:
    rows=int(input("Enter a Number  : "))
    if rows<=0:
        print("Enter positive integer")
    else:
        pyramid(rows)
except ValueError:
    print("Invalid input")