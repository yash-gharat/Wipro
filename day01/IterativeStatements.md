# Iterative statement - statement needs to execute multiple times

| Statement | Description                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------------------- |
| for       | Executes a block of code multiple times, with a specified start, end, and increment/decrement                  |
| while     | Executes a block of code repeatedly as long as a specified condition is true                                   |
| do-while  | Executes a block of code once, and then repeatedly executes the block as long as a specified condition is true |

```
for-loop
{init
condition
body
updation}

for(init;condition;updation){}
for(i=1;i<=10;i++/i=i+1)
	display "hello"
end-for

```

# Question 1

- Write a pseudo-code to calculate the factorial of a given number.
  Example: factorial of 5 = 5*4*3*2*1 = 120.
  Note 1: Factorial of 0 is 1.
  Note 2: You can drag and drop the required number of pseudo-code magnets into the pseudo-code box.
  Estimated Time: 15 minutes

- Using for loop
```
input Number
result = 1
if(Number < 0) then
    display "cannot define fact for negative number"
else if(Number=0) then
    display result
else
    for(i=1;i<=Number;i=i-1)
    result = result \* i
    display result
    end-for
```

-using while loop
```
input Number
result=1
if(Number==0) then
    display result
end-if

while(Number!=0) do
result=result\*Number
Number=Number-1
end-while

display result

```



