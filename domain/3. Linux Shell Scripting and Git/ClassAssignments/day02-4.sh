# Prompt the user to enter a number
read -p "Input a number: " n
 
# Check if the number is greater than 100
if [ "$n" -gt 100 ]; then
    echo "The number is greater than 100."
else
    echo "The number is not greater than 100."
fi

