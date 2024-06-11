BEGIN{
count=0
}
$2 == "manager" || $2 == "peon"{
print $0
count++
}
END{
print "Total emp: ",count
}
