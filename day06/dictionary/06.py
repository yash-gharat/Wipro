# Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
# The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
# The function should identify the degree of correctness as mentioned below:

# CORRECT, if it is an exact match

# ALMOST CORRECT, if no more than 2 letters are wrong

# WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

# and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
# Assume that the words contain only uppercase letters and the maximum word length is 10.
 
# Sample Input
# {"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
	
# Expected Output
# [2, 2, 1]

def find_correct(dict):
    count = {
        "correct_count" : 0,
        "almost_correct_count" : 0,
        "wrong_count" : 0
    }
    # itreate over the dict
    for k,v in dict.items():
        # If key equals value, increment correct count
        if k == v:
            count["correct_count"] += 1
        else:
            # If lengths are equal, check for almost correct or wrong
            if len(k) == len(v):
                diff_count = 0
                #itrate over the character
                for i in range(len(k)):
                    # print(i)
                    # Compare char and count diff
                    if k[i] != v[i]:
                        diff_count += 1
                # If differences are less than or equal to 2 => almost correct
                if diff_count <= 2:
                    count["almost_correct_count"] += 1
                # If differences are more than  2 =>wrong
                elif diff_count > 2 :
                    count["wrong_count"] += 1
            else: 
                count["wrong_count"] += 1
    return (list(count.values()))

dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}

print(find_correct(dict))