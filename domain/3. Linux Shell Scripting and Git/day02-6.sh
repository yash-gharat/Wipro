read -p "Enter a number: " num

if [ "$num" -gt 0 ]; then
    echo "Number is positive"
elif [ "$num" -lt 0 ]; then
    echo "Number is negative"
else
    echo "Number is zero"
fi

