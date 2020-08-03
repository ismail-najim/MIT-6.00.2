###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    current_limit = limit
    remaining_cows = cows.copy()
    final_list = []
    current_list = []
    cows_inmars = True
    
    # As long as there are cows in mars - keep bringing the ship to get them out
    while cows_inmars:
        
        not_done = True
        
        # As long as there is space in ship - Review current list and pick cow that fits
        while not_done: 
        
            # Create a dictionary that only has cows that fit
            fit_cows = remaining_cows.copy()
            fit_cows_iter = fit_cows.copy()
            for k in fit_cows_iter:
                if fit_cows_iter[k] > current_limit:
                    del fit_cows[k]
            
            # If dictionary empty - then no more cow for this round - reinitialize all
            if len(fit_cows) == 0:
                final_list.append(current_list)
                current_list = []
                current_limit = limit
                not_done = False
                break
            
            # Identify the heaviest cow that fits and put in the spaceship
            max_weight = max(fit_cows.values())
            for k in fit_cows:
                if fit_cows[k] == max_weight:
                    current_list.append(k)
                    del remaining_cows[k]
                    current_limit =current_limit - max_weight
                    break
        
        if len(remaining_cows) == 0:
            cows_inmars = False
            break
                
    return final_list
        
        


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Initialize parameters
    cows_ = cows.copy()
    fit_partition = []
    partitions = []
    
    # Go through the partitions      
    for partition in get_partitions(cows_):   
        unfit_partition = 0
        
        # Check that all trips in the partition are under the limit
        for trip in partition:
            weight = 0
            
            # Calculate trip weight
            for k in trip:
                weight += cows_[k]
            
            # Check that trip is under limit weight
            if weight > limit:
                unfit_partition = 1
                break
            
        
        # Check if partition works and expose it
        if unfit_partition == 0:
            return partition
            break
    
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
   
    start = time.time()
    print(greedy_cow_transport(cows,limit))

    end = time.time()
    print(end - start)
   
    start = time.time()
    print(brute_force_cow_transport(cows,limit))
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


