addtwo () {
       sum=$(( $1 + $2 ))
       return $sum
}

difftwo () {
           dif=$(( $1 - $2 ))
            return $dif
}
addtwo 115 16
total=$?

difftwo  115 16

diff=$?

echo "$total"

echo "$diff"
