BEGIN{
count=0
}
$4 > 40000 {
    print $1 " with salary " $4
    count++
}
END {
    print "Total emps salary more than 40000:", count
}
