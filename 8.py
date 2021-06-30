line=input().split()
line1=input().split()
line_s=set(line)
line_s1=set(line1)
res=line_s.intersection(line_s1)
thislist=list(res)
for i in range(len(thislist)):
    thislist.sort()
    print(thislist[i])