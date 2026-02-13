matrix=[]
for _ in range(5):
    matrix.append([int(ch) for ch in input().split()])

count=0
for i in range(len(matrix)):
    if sum(matrix[i])==1:
        count+=abs(2-i)
        idx=matrix[i].index(1)
        count+=abs(2-idx)
print(count)
