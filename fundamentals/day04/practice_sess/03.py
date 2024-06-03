# Write a python program which displays the count of the names that matches a given pattern from a list of names provided.
# Consider the pattern characters to be:
# 1. "_ at" where "_" can be one occurrence of any character
# 2. "%at%" where "%" can have zero or any number of occurrences of a character

# Sample Input
# [Hat, Cat, Rabbit, Matter]
# Expected Output
# _at -> 2
# %at% -> 3

def names_pattern(names,patterns):
    # Create an empty object to store counts for each pattern
    pattern_counts = {}

    for pattern in patterns:
        # Init count for current pattern
        count = 0
        for name in names:
            # Check if the name matches the pattern
            if is_matching_pattern(name, pattern):
            # Increment count if name matches pattern
                count += 1
        pattern_counts[pattern] = count  

    print( pattern_counts)


def is_matching_pattern(name, pattern):
    # If pattern has '_', it matches any single character
    if '_' in pattern:
        return name[0] == pattern[0] and name[-1] == pattern[-1]
 
    elif '%' in pattern:
        return pattern[1:-1] in name
    return False



names = ['Hat', 'Cat', 'Rabbit', 'Matter']
patterns = ['_at', '%at%']

names_pattern(names,patterns)
