#Even or odd

read -p "Enter a number: " num
#if  [ $((num%2)) -eq  0 ]; then
if [ `expr $num % 2` == 0 ]; then
	echo "Even"
else
	echo "Odd"
fi
