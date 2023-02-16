"""Question three for an executable examination."""

from pathlib import Path
from typing import List

# TODO: Question 3a. {{{

# Instructions:
# Provide the source code lines in this function
# so that it operates in the specified fashion

# Function description:
# The function input_file should:
# --> Accept as input a file_name that is of type string
# --> Assume that the program that runs the function will
#     be executed from the root of the GitHub repository;
#     as in "python source/question_three.py"
# --> Construct a pathlib Path object and then read in the
#     values from the file and store them as strings in a list
# --> Return a list of strings containing all of the values
#     that were stored inside of the file.
# --> For instance, the inputs/observations.txt file contains these values:
#     5
#     7
#     9
#     11
#
#     This means that it would cause this function to produce the output:
#     ['5', '7', '9', '11']


def input_file(file_name: str) -> List[str]:
    """Use a pathlib Path object to read and return the contents of the specified file."""
    return [""]


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    question_three_output_a = input_file("inputs/observations.txt")
    return question_three_output_a


# }}}

# TODO: Question 3b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function convert_list should:
# --> Accept as input a variable called input_list that contains a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a list of all the converted int values
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output [5, 7, 9, 11]


def convert_list(input_list: List[str]) -> List[int]:
    """Convert a list of strings to a list of int values."""
    output_list_int = []
    for input_value in input_list:
        input_value_int = str(input_value)
        output_list_int.append(output_list_int)
    return output_list_int


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    question_tree_output_b = convert_list(['5', '7', '9', '11'])
    return question_tree_output_b

# }}}

# TODO: Question 3c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function sum_list should:
# --> Accept as input a list of int values
# --> Compute the sum of all of the int values in the list
# --> Return the sum of all the int values in the list
# --> For instance, if the function receives [5, 7] as
#     an input it returns the value of 12 stored in an int variable


def sum_list(input_list: List[int]) -> int:
    """Sum all of the values inside of a list of int values."""
    return 0


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    question_three_output_c = sum_list([5, 7, 9, 11])
    return question_three_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
