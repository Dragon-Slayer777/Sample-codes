l = l1 = l2 = l3 = []
q = int(input("enter number of elements"))
for t in range(q):
    c=int(input("enter value"))
    l+=[c]
#if number is even enters list one ; if odd list two ; if prime then three
def primecheck(x):
    for i in range(1,x):
        if x%i==0:
            break
        else:
            return x
for j in l:
    if j%2 == 0:
        l1+=[j]
    elif j%2!=0:
        l2+=[j]
    elif primecheck(j)==j:
        l3+=[j]
print(l1,l2,l3,sep="\n")



