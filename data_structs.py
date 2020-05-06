n = int(input("enter number of elements"))
l =[]
for k in range(n):
    x = int(input("enter value"))
    l+=[x]
i = 1
newl = []
for j in l:
    if j>0:
        newl += [j]
print("positive numbers in range =","\t",newl)
t = (1,2,3,4,5,6,7,8,9)
x = int(input("enter element to remove"))
lis =[]
for i in range(0,len(t)):
    if t[i] == x:
      pass
    else:
        lis+=[t[i]] 
print(lis)
d = dict(zip(('a','b','c'),(1,2,3)))
y = input("enter value to remove")
d.pop(y)
print(d)
<<<<<<< HEAD

        



    
=======
>>>>>>> 40fe566d3f45e3c25864f818902521b6e7690f21
