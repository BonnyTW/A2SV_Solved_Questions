t= int(input())

for _ in range(t):
    n=int(input())
    r=[int(ch) for ch in input().split()]
    m=int(input())
    b=[int(ch) for ch in input().split()]

    max_r=0
    psum_r=0
    for num in r:
        psum_r+=num
        max_r=max(psum_r,max_r)

    max_b=0
    psum_b=0
    for num in b:
        psum_b+=num
        max_b=max(psum_b,max_b)

    print(max_r+max_b)
    
    

