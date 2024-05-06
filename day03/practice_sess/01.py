# Write a  program to print all natural numbers between 1 to n using recursion.

#  fn(num)
#  check if n > =1 
#   add it to the []
#  recursion=> fn(n-1,list)
#  print list

def print_natural_numbers(n,list=[]): #4
    if n >= 1:
        print_natural_numbers(n-1,list)
        list.append(n)
    print(list)
n = 4
print_natural_numbers(n)

