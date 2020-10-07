n=int(input("how many elements do u want in your list_1:"))
a=[]
for i in range(0,n,1):
    a.append(int(input("enter the element:")))
print("List_1=",a)
a.sort()
print(a)
print("Maxium number:",a[-1])
print("Second largest number :",a[-2])


m=int(input("how many elements do u want in your list_2:"))
b=[]
for i in range(0,m,1):
    b.append(int(input("enter the element:")))
print("list_2=",b)
#adding 2 lists
c=a+b
print("Addition of List_1 and List_2:",c)
c.sort()
print("Sorted list:",c)
# swapping 1st and last element
temp=c[0]
c[0]=c[-1]
c[-1]=temp
print("List after swapping 1st and last element:",c)