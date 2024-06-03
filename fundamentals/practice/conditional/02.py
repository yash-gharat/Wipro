# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), 
# $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter the age"))
day = "Wednesday"
adult_movie_ticket = 12
child_movie_ticket = 8
discount = 2
if day =="Wednesday":
    if (age >= 18):
        adult_movie_ticket -= discount    
        print(adult_movie_ticket)
    else:
        child_movie_ticket -= discount
        print(child_movie_ticket)
        
