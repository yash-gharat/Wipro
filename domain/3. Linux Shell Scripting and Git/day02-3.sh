read -p "Enter num1: " num1 
read -p "Enter num2: " num2
read -p "Enter the operation (+,-,*,/): " operation
result = $(($num1 $operation $num2 ))
echo "$num  $operation  $num2  =  $result "
