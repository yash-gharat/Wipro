# read a num from console and check  if divisble by 5 or not
read -p "Enter a num: " num
#if [ $(( num % 5 )) -eq 0 ]; then
if (( num % 5 == 0 )); then
echo "Divisile by 5"
else
echo "Not divisble by 5"
fi
