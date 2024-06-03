#list of passengers
passengers_list=["George","Annie", "Jack","Annie","Henry", "Helen","Maria","George","Jack","Remo"]
 
#set function - removes the duplicates from the list and returns a set
unique_passengers=set(passengers_list)
print("removes the duplicates",unique_passengers)
 
#creating a set
flight_set={500,520,600,345,520,634,600,500,200,200}
print("creating a set",flight_set)
 
flights_at_src = ["AI230","BA944","EM395","AI704","BA944","AI704"]
flights_at_dest = ["SI107","AI034","EM395","AI704","BA802","SI236"]
print(flights_at_src)
print(flights_at_dest)
 
#Creating list of unique flights at source and destination
uniq_src_flights = set(flights_at_src)
uniq_dest_flights = set(flights_at_dest)
print("Creating list of unique flights at source ",uniq_src_flights)
print("Creating list of unique flights at destination ",uniq_dest_flights)
 
 
#setA-setB -> Gives the elements that are only in setA
#List of flights only at source airport
flights_only_at_src = uniq_src_flights-uniq_dest_flights
print("List of flights only at source airport setA-setB",flights_only_at_src)
 
#setA&setB -> Gives the common elements between setA and setB
#List of flights common to source and destination airports
common_flights=uniq_src_flights&uniq_dest_flights
print("common elements between setA & setB",common_flights)
 
#setA|setB -> merges setA and setB after removing duplicates
#List of all flights at source and destination airports
all_flights=uniq_src_flights|uniq_dest_flights
# all_flights.sort(reverse=True)
print("setA|setB",all_flights)
print("setA|setB",sorted(all_flights))

# test = {0,5,4,1,6,9,3,2}
# print(sorted(test))