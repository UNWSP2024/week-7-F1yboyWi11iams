# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    def get_values():
    all_entered_values = []
    year = int(input("Please enter a year: "))
    name_of_state = input("Please enter the name of a state: ")
    population = int(input("Please input the population of that state fir that particular year: "))
    again = 'y'
    again = input('y = yes, anything else = no: ')
    get_values()
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    # Now have the user enter a year. 
    int(input("Enter a year: ")
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    total_population = for population in range(input("Enter a year: "))

    # print the totalled population
    print(total_population)


# Call the main function.
if __name__ == '__main__':
    main()
