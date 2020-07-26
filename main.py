import os, sys

import brute_force_method as bfm
import greedy_method as gm

def write_to_file(shortest_common_string, method):
    print("----------------------------------------------------------------------")
    try:
        with open("output_file.txt", "w") as writer:
            writer.write("Shortest Common String using {0} is: {1}" .format(method, shortest_common_string))
        print("Output File update with result.")
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print("Unexpected error while writing file:", sys.exc_info()[0])
        print("Shortest Common String using {0} is {1}" .format(method, shortest_common_string))
    

def find_shortest_common_string(content):
    """ Accepts the content as argument and provide options to choose
        the method to find the shortest common string.
    """
    shortest_common_string = None
    print("----------------------------------------------------------------------")
    print("1. Use Brute Force Method\n2. Use Greedy Method")
    print("----------------------------------------------------------------------")
    # getting the user choice
    choice = input("Select your method.")
    print("----------------------------------------------------------------------")
    # checking the choice
    if choice == '1':
        shortest_common_string = bfm.shortest_common_string(content)
        print("Using Brute Force Method: ", shortest_common_string)
    elif choice == '2':
        shortest_common_string = gm.greedy_shortest_common_string(content)
        print("Using Greedy Method: ", gm.greedy_shortest_common_string(content))
    else:
        print("Please enter a valid choice")
        find_shortest_common_string(content)
    write_to_file(shortest_common_string, 'Brute Force Method' if choice == '1' else 'Greedy Method')

def get_data(file):
    """ Read data from input file - input_file.txt
        Return string array.
    """
    try:
        # opening file in read mode
        with open(file, 'r') as file_reader:
            content = file_reader.read().split("\n")
            if not content:
                print("No data found.")
                find_shortest_common_string(get_data())
            else:
                return content                   
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print("Unexpected error while reading file: ", sys.exc_info()[0])
        find_shortest_common_string(get_data())

#find_shortest_common_string(get_data("input_file.txt"))