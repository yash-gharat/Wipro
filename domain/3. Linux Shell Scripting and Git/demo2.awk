$2 == "manager" {
total += $4
}
END{
print "Total:", total
}
