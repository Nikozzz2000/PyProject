p = int(input("назавите ваше число:"))
i = 0
if p == 10:
    print(1)
elif p < 10:
    print(p)
else:
    while p > 0:
        n = p % 10
        p = p//10
        if n > i:
            i = n
    print(i)
