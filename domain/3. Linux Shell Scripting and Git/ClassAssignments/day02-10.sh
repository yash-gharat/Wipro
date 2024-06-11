#biggest of 3 nos
read -p "Enter num1: " num1
read -p "Enter num2: " num2
read -p "Enter num3: " num3

max=$(( num1 > num2 ? num1 : num2 ))
max=$(( max > num3 ? max : num3 ))

echo "The biggest number is: $max"
