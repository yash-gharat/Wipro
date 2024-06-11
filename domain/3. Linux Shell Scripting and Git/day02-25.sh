a=5
b=3

sum=$(expr $a + $b)
echo "Sum: $sum"

difference=$(expr $a - $b)
echo "Difference: $difference"

product=$(expr $a \* $b)  # Note the escaped asterisk
echo "Product: $product"

quotient=$(expr $a / $b)
echo "Quotient: $quotient"

remainder=$(expr $a % $b)
echo "Remainder: $remainder"
