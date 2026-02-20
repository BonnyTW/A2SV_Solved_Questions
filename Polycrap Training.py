n=int(input())
contest=[int(ch) for ch in input().split()]
contest.sort()


count=0
j=1
for i in range (n):
    if contest[i] >= j:
        count+=1
        j+=1
    else:
        continue
        

print(count)




