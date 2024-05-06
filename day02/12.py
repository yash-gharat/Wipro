def bubble_sort_passes(list):
    # Print the original list
    print("Original list:", list)
    # Initialize the number of passes
    passes = 0
    # Outer loop for each pass
    for i in range(0,len(list)):
        # Initialize swapped flag
        swapped = False
        # Inner loop for comparisons and swaps
        for j in range(len(list) - i - 1):
            # Compare adjacent elements
            if list[j] > list[j + 1]:
                # Swap 
                list[j], list[j + 1] = list[j + 1], list[j]
                # Set swapped flag to True
                swapped = True
        # Increment the number of passes
        passes += 1
        # If no swaps were made in this pass, the list is sorted, so break out of the loop
        # if not swapped:
        #     break
    # Print the number of passes required
    return print("Number of passes required:", passes)


num_list = [67, 34, 8, 22, 23]
bubble_sort_passes(num_list)
