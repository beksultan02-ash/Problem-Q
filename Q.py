def sum(n):
    if n == 0:
        return 0
    return (n % 10) + sum(n // 10)

n=int(input())
if (sum(n) % (n%10) )==0:
    print("Yes")
else:
    print("No")