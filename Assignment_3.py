#1.Rename key city to location in the following dictionary
SkillSanta_Dict={
    "name":"Sachin",
    "age":22,
    "salary":60000,
    "city":"New Delhi"
}
SkillSanta_Dict["location"]=SkillSanta_Dict.pop("city")
print(SkillSanta_Dict)
#%%
#2.Given a list iterate it and count the occurrence of each element and create 
#   a dictionary to show the count of each element
lis=[11,45,8,11,23,45,23,45,89]
dic={}
for i in lis:
    if i not in dic:
        dic[i]=0
    dic[i]+=1
print(dic)
#%%
# 3.Remove duplicate from a list and create a tuple and find the minimum 
#    and maximum number
samplelist=[87,45,41,65,94,41,99,94]
unique_items=[]
for i in samplelist:
    if i not in unique_items:
        unique_items.append(i)
print("unique_items",unique_items)

def convert(list):
    return tuple(i for i in list)
print("tuple",convert(unique_items))

unique_items.sort()
print("min:",unique_items[0])
print("max:",unique_items[len(unique_items)-1])
#%%
# 4.Create a function showEmployee() in such a way that it should accept employee
#   name, and it’s salary and display both, and if the salary is missing in 
#   function call it should show it as 50000
def showEmployee(name,salary=50000):
    employee_name=name
    employee_salary=salary
    print("Employee {} salary is:{}".format(employee_name,employee_salary))
showEmployee("Eddy",50000)
showEmployee("Eddy")
#%%
# 5.Create an inner function to calculate the addition in the following way
#    ● Create an outer function that will accept two parameters a and b
#    ● Create an inner function inside an outer function that will calculate
#     the addition of a and b
#    ● At last, an outer function will add 5 into addition and return it
def outer(a,b):
    def inner(a,b):
        sum=a+b
        return sum
    sum=inner(a,b)
    return sum+5
outer(5,4)
#%%
# 6.Write a recursive function to print the fibonacci series of n numbers
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n=10
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i))
#%%
# 7.Assign a different name to function and call it through the new name
#    Example:
#       the function displayStudent(name, age). Assign a new name showStudent(name,
#       age) to it and call through the new name
def displayStudent(name, age):
    print("Name of Student:",name)
    print("Age of Student:",age)
showStudent=displayStudent
showStudent("Nikhil",20)
#%%
# 8.Create a python function which takes a mobile number from the user until
#   the user would not give you a proper mobile number. If a user gives the
#   wrong input you have to take input again from the user, once get proper
#   number stop asking
def mobilenumber():
    while(1>0):
        number=input("Enter the mobile no:")
        if(len(number))==10:
            break
        else:
            continue
mobilenumber()
#%% 
# 9.Write a Python function that accepts a string and calculates the number of
#   uppercase letters and lowercase letters.
#    Sample String : 'The quick Brown Fox'
#   Expected Output :
#   No. of Uppercase characters : 3
#   No. of Lowercase Characters : 13
def counts(str):
    lis=str.split()
    upper=0
    lower=0
    for i in lis:
        for j in i:
            if j==j.upper():
                upper+=1
            else:
                lower+=1
    print("No. of Uppercase characters :",upper)
    print("No. of Lowercase Characters :",lower)
    
counts('The quick Brown Fox')
#%%
# 10.Write a Python function to check whether a number is perfect or not. Go
#    to the editor According to Wikipedia : In number theory, a perfect number is
#    a positive integer that is equal to the sum of its proper positive divisors,
#    that is, the sum of its positive divisors excluding the number itself (also
#    known as its aliquot sum). Equivalently, a perfect number is a number that
#    is half the sum of all of its positive divisors (including itself).
#    Example : The first perfect number is 6, because 1, 2, and 3 are its proper
#   positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to
#   half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next
#    perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect
#    numbers 496 and 8128.
def perfectnumber(n):
    sum=0
    for i in range(1,n+1):
        if(n%i==0):
            sum=sum+i
    #print(sum)
    if(sum/n==2):
        print("{} is a perfect number".format(n))
    else:
        print("{} is a not perfect number".format(n)
              
#perfectnumber(8128)

#%%
    
                





















      