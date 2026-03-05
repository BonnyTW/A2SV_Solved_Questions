n,k,q=[int(ch) for ch in input().split()]

recipes=[]
for i in range(n):
    l,r=[int(ch) for ch in input().split()]
    recipes.append((l,r))

questions=[]
for i in range(q):
    l,r=[int(ch) for ch in input().split()]
    questions.append((l,r))

freq=[0]*(200000+2)

for l,r in recipes:
    freq[l]+=1
    freq[r+1]-=1


for i in range(1,len(freq)):
    freq[i]=freq[i]+freq[i-1]

for i in range(len(freq)):
    freq[i]=1 if freq[i]>=k else 0

for i in range(1,len(freq)):
    freq[i]=freq[i]+freq[i-1]


for l,r in questions:
    print(freq[r]-freq[l-1])