#for ((i=10; i>=0; i--))
#do
#    echo $i
#done

ctr=9
while [ $ctr -gt 0 ]
do
echo $ctr
((ctr--))
done
