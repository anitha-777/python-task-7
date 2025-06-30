# 1)	From the list nums = [10, 25, 30, 45, 50, 60], create a set of numbers where the number is divisible by 5 but not divisible by 10 using set                 comprehension.

nums = [10, 25, 30, 45, 50, 60]
s={i for i in nums if i%5==0 and i%10!=0}
print(s)

# 2)	Write a program to sum the digits of all numbers in a list.
#     Example: [12, 34, 5] ➞ 1+2 + 3+4 + 5 = 15

x=[12, 34, 5]
y=sum(x)
print(y)

# 3)	Create a new list by repeating elements of a list n times.
#              Example: [1, 2, 3], n = 2 ➞ [1, 2, 3, 1, 2, 3]
x=[1, 2, 3]
n = 2 
print(x*2)

# 4)	Write a function to count frequency of each element in a list (return as dictionary).
a= [10, 25, 30, 45, 50,10,30,80,60,90,60]
l1=[]
for i in a:
    if i not in l1:
       x=a.count(i)
       y=f"{i} : {x}"
       l1.append(y)
print(l1)

# 5)	Write a function to count how many prime numbers exist in a given range.

def prime_count(a):
    is_prime=False
    ct=0
    for i in range(2,a):
        for j in range(2,i):
            if i%j==0:
               is_prime=True
               break
            else:
                is_prime=False
        if is_prime==False:
              ct+=1
    return ct
print(prime_count(10))


# 6)	Write a function to calculate the sum of digits of a number until a single-digit result is obtained.
#   Example: 9875 ➞ 9+8+7+5=29 ➞ 2+9=11 ➞ 1+1=2


def single_digit(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n//=10
    print(sum)
    if sum>=10:
        single_digit(sum)
single_digit(9875)
    

