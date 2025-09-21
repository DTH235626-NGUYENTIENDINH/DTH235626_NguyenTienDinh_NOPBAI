i = int(input("i: "))
j = int(input("j: "))
k = int(input("k: "))
if i<j:
    if j<k:
        i=j
    else:
        j =k
else:
    if j>k:
        i=j
    else:
        i=k
print("i:",i," j:",j," k:",k)