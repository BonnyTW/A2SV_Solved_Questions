t = int(input())
 
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
 
for _ in range(t):
    s = input()
    n = len(s)
    ans = set()  
    
    for c in alphabet:
        i = 0
        possible = True  
 
        while i < n:
            if s[i] == c:
                if i + 1 < n and s[i + 1] == c:
                    i += 2  
                else:
                    possible = False
                    break
            else:
                i += 1  
 
        if not possible:
            ans.add(c)
 
    print("".join(sorted(ans)))
