#1
n = int(input("enter the number of terms: "))
i = 1
count = 0
for i in range(n):
    i += 1
    y = 1/i
    count += y
print(round(count,9))

#2
num=int(input("enter the number:"))
fact=1
i=1
sum=0
while i<=num:
    fact=fact*i
    i+=1
    sum+=1/fact
print("the sum of the series is:",round(sum,9))

#3
num=int(input("enter the number:"))
x=int(input("enter the numerator:"))
sum=0
i=1
while i<=num:
    sum+=(1+(x**i)/i)
    i+=1
print("the sum of the series is:",round(sum,9))
