n = int(input('number of terms{not less than 3}'))
f1 = f2 = 1
print(f1,f2,end= " ")
for i in range(n-2):
    f3 = f1 + f23
    f1 = f2
    f2 = f3
    print(f3,end = " ")
