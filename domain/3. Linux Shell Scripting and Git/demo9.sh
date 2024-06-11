addtwo () {
       sum=$(( $1 + $2 ))
       return $sum
}

# Invoke your function
addtwo  15 16

# Capture value returnd by last command
result=$?

echo "Sum  = $result"
