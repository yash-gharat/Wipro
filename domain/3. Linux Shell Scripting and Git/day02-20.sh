#!/bin/bash
 
#reading data from the user
read -p 'Enter a : ' a
read -p 'Enter b : ' b
 
if(( $a==$b ))
then
    echo a is equal to b.
else
    echo a is not equal to b.
fi
 
if(( $a!=$b ))
then
    echo a is not equal to b.
else
    echo a is equal to b.
fi
 
if(( $a<$b ))
then
    echo a is less than b.
else
    echo a is not less than b.
fi
 
if(( $a<=$b ))
then
    echo a is less than or equal to b.
else
    echo a is not less than or equal to b.
fi
 
if(( $a>$b ))
then
    echo a is greater than b.
else
    echo a is not greater than b.
fi
 
if(( $a>=$b ))
then
    echo a is greater than or equal to b.
else
    echo a is not greater than or equal to b.
fi
