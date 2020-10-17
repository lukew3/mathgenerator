x = int(input("Enter X : "))
y = int(input("Enter y : "))
gcd = 1
if x % y == 0:
    print(y)
for k in range(int(y / 2), 0, -1):
    if x % k == 0 and y % k == 0:
        gcd = k
        print(gcd)
        break 