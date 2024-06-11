AGE=$1

if [ $AGE -lt 13 ]; then
    echo "Kid"
elif [ $AGE -lt 20 ]; then
    echo "Teenager"
elif [ $AGE -lt 65 ]; then
    echo "Adult"
else
    echo "Elder"
fi

