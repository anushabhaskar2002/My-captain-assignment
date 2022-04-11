str = input ("enter the string")
d = dict()
for c in str:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
a = sorted(d.items(), key=lambda x: x[1], reverse=True)    
for x in range(len(a)):
    print(a[x][0]," = ",a[x][1])
