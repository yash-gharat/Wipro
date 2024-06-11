sum=0
for i in {1..10}; do
    if [ $((i % 2)) -ne 0 ]; then
        sum=$(expr $i + $sum)
    fi
done
echo "Sum of odd numbers is: $sum"

