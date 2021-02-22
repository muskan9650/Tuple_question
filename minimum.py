b=(50, 40, 23, 70, 56, 12, 5, 10, 7)
a=list(b)
print(a)
# min=min(b)
# print(min)
max=a[0]
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
        print(max)