line=input().split()
min=1000
for i in range(len(line)):
    k=int(line[i])
    if k<min and k>0:
        min=k
print(min)