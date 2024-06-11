BEGIN{
peon_count=0
manager_count=0
manager_salary=0
peon_salary=0
}
$2 == "peon"{

peon_count++
peon_salary += $4
}
$2 == "manager"{
manager_count++
manager_salary += $4
}
END{
print "Total peon: ", peon_count
print "Total peon salary", peon_salary
print "Total managers: ", manager_count
print "Total manager salary: ",manager_salary
}
