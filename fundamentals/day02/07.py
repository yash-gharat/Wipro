# Problem Statement
# The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
# Rate per Adult: Rs. 37550.0
# Rate per Child: 1/3rd of the rate per adult
# Service Tax: 7% of the ticket amount (including all passengers)
# As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
# Find and display the total ticket cost for a group which had adults and children.
# Test the program with different input values for number of adults and children.
# Test the program with different input values for number of adults and children.

# Sample Input
# Number of adults 5
# Number of children 2
# Expected Output
# Total Ticket Cost: 204910.35

def calculate_ticket_cost(no_of_adults, no_of_children):
    rate_per_adult = 37550.0
    rate_per_child = rate_per_adult / 3
    service_tax_rate = 7
    discount_rate = 10
    #add service tax
    cal_service_tax = 1 + (service_tax_rate/100)
    #substract discount
    cal_discount_rate =1 - (discount_rate/100)
    
    total_adult_cost = no_of_adults * rate_per_adult
    #187750
    total_child_cost = no_of_children * rate_per_child
    #25033.3333333
    total_ticket_cost = round(((total_adult_cost + total_child_cost)* (cal_service_tax) * (cal_discount_rate)),2)
    #(212783.333333) * (1.07) * (0.9)
    return  total_ticket_cost


no_of_adults = 5
no_of_children = 2

total_ticket_cost = calculate_ticket_cost(no_of_adults, no_of_children)
print("Total Ticket Cost:",total_ticket_cost)
