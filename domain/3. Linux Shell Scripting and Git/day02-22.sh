read -p "Enter the amount: " amount

if [ "$amount" -gt 5000 ]; then
    discount=$((amount * 5/100))
    final_amt=$((amount - discount))
    echo "Final amount after 5% discount: $final_amt"
else
    echo "No discount applied: $amount"
fi
