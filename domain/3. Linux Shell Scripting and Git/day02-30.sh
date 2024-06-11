read -p "Enter a number: " num
fact=1
i=$num
while [ $i -gt 1 ]; do
    fact=$(( fact * i ))
    ((i--))
done
echo "The factorial of $num is: $fact"

