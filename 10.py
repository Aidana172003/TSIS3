'''n=int(input())
d=dict(input().split() for i in range(n))
k=input()'''
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])