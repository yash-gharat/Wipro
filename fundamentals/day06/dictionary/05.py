# Care hospital wants to know the medical speciality visited by the maximum number of patients. 
# Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. 
# The details of the medical specialities are stored in a dictionary as follows:
# {
# "P":"Pediatrics",
# "O":"Orthopedics",
# "E":"ENT
# } 
# Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
# Note: 
# Assume that there is always only one medical speciality which is visited by maximum number of patients.
# Perform case sensitive string comparison wherever necessary.
# Sample Input
# [101,P,102,O,302,P,305,P]
# [101,O,102,O,302,P,305,E,401,O,656,O]
# [101,O,102,E,302,P,305,P,401,E,656,O,987,E]
	
# Expected Output
# Pediatrics
# Orthopedics
# ENT

def fn(list):
    speacialty = {
        "P":"Pediatrics",
        "O":"Orthopedics",
        "E":"ENT"
        }
    max_count = {
        "P" : 0,
        "O" : 0,
        "E ": 0    
        }
    
    for i in list[1::2]:
        # print(i)
        max_count[i] += 1
        # print(list)
    max_specialty = max(max_count, key=max_count.get)
    specialty = speacialty[max_specialty]
    return print("MAximum : ",specialty)

list = [101,'P',102,'O',302,'O',305,'O']
fn(list)

# Sample Input

# Expected Output
# Pediatrics
# Orthopedics
# ENT