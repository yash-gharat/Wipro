for i in {1..10}; do
    if [[ $i -eq 6 || $i -eq 8 ]]; then
        continue
    fi
    echo $i
done
