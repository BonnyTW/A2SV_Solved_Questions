from collections import Counter
m=int(input())

for _ in range(m):
    s=input()
    t=input()

    s_list=list(s)
    t_list=list(set(t))
    t_list.sort()

    s_counter=Counter(s)
    t_counter=Counter(t)

    i=0
    j=0

    ans=[]

    # check if impossible
    impossible = False
    for ch in s_counter:
        if t_counter[ch] < s_counter[ch]:
            impossible = True
            break
    if impossible:
        print("Impossible")
        continue


    while i < len(s_list) and j < len(t_list):
        if s_list[i]==t_list[j]:
            ans.append(s_list[i])
            i+=1
        elif s_list[i]>t_list[j]:
            count_ch=t_counter[t_list[j]]-s_counter[t_list[j]]
            ans.append(count_ch*t_list[j])
            j+=1
        else:
            ans.append(s_list[i])
            i+=1
    ans.extend(s_list[i:])
    while j < len(t_list):
        count_ch=t_counter[t_list[j]]-s_counter[t_list[j]]
        ans.append(count_ch*t_list[j])
        j+=1
    print(''.join(ans))



