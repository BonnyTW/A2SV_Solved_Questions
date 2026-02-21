t=int(input())

for _ in range(t):
    n,k = [int(ch) for ch in input().split()]
    current_coin=k
    arr=[]
    for i in range(n):
        arr.append([int(ch) for ch in input().split()])

    arr=sorted(arr,key=lambda x :x[2])
    

    for l_i,r_i,real_i in arr:
        if l_i <= current_coin:
            if real_i>=current_coin:
                current_coin=real_i
    print(current_coin)
