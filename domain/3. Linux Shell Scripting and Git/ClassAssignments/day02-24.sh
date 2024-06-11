read -p "Enter the first number:" num1
read -p "Enter the second number:" num2
if [ $num1 -eq $num2 ]; then
    echo "The numbers are equal."
elif [ $num1 -lt $num2 ]; then
    echo "$num1 is less"
else
    echo "$num2 less"
fi
