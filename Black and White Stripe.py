from collections import Counter
t=int(input())

for _ in range(t):
    n,k=[int(ch) for ch in input().split()]
    s=input()

    count=Counter(s[:k])
    ans=count['W']
    for right in range(k,n):
        count[s[right]]+=1
        count[s[right-k]]-=1
        ans=min(ans,count['W'])
    print(ans)
