n = int(input("enter the number of rows: "))
#outer loop
for i in range(1, n+1):
#inner loop
    for i in range(i):
#print star
        print('*', end=' ')
#after each row
    print()