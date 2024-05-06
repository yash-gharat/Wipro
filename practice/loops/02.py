# . Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 4
sum = 0
for i in range(0,n+1):
    # print(i)
    if (i % 2 == 0):
        sum += i
print(sum)