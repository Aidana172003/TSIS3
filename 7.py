line=input().split()
line1=input().split()
line_s=set(line)
line_s1=set(line1)
res=line_s.intersection(line_s1)
counter=0
for i in range(len(res)):
    counter+=1
print(counter)