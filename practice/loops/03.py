#  Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, 
# but skip the fifth iteration.

n = 2

for i in range(1,10):
    if(i == 5):
        continue
    else:
        print(f"{n}X {i} = {n * i}" )
        