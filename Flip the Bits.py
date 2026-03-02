from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(ch) for ch in input()]
    b=[int(ch) for ch in input()]

    j=n-1
    count=Counter(a)
    flipped=False
    possible=True

    while j>=0:
        curr = a[j]
        if flipped:
            curr = 1-curr

        if curr==b[j]:
            count[a[j]] -= 1
            j -= 1
        else:
            if count[0] == count[1]:
                flipped = not flipped
                count[a[j]] -= 1
                j -= 1
            else:
                possible=False
                break

    if possible:
        print('YES')
    else:
        print('NO')
