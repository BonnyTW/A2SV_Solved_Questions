
def swap_case(s):
    ans=[]
    for i in range (len(s)):
        if 'A'<=s[i]<='Z':
            ans.append(chr(ord(s[i])+32))
        elif 'a'<=s[i]<='z':
            ans.append(chr(ord(s[i])-32))
        else:
            ans.append(s[i])
    return ''.join(ans)
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
