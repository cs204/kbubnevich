s=input()
s1=""
i=0
for c in s:
    if c==' ':
        c='...'
        i+=1
    s1+=c
print(s1)