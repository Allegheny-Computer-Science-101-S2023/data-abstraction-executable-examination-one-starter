"""Question one for an executable examination."""

# TODO: Question 1a. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function determine_even_odd should:
# --> Return "even" (of type string) when the input variable (of type int)
#     contains an even number as its value
# --> Return "odd" (of type string) when the input variable (of type int)
#     contains an odd number as its value


def determine_even_odd(value: int) -> str:
    """Determine if a number is even or odd."""
    if value % 2 == 1:
        return "even"
    return "odd"


def question_one_a():
    """Run question one-a."""
    # Do not edit this function
    space = " "
    question_one_output_a = determine_even_odd(10)
    question_one_output_a = question_one_output_a + space + determine_even_odd(11)
    question_one_output_a = question_one_output_a + space + determine_even_odd(-11)
    question_one_output_a = question_one_output_a + space + determine_even_odd(0)
    return question_one_output_a


# }}}

# TODO: Question 1b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function compute_square should:
# --> Accept as input a variable called value of type int
# --> Produce as output an int that is the square of the input value
# --> For instance, an input of 5 would produce the output of 25
# --> The function must use a while loop to perform the computation


def compute_square(value: int) -> int:
    """Compute the square of a number through iteration with a while loop."""
    num_iterations = 1
    answer = 0
    while num_iterations < value:
        answer = answer + value
        num_iterations = num_iterations + 1
    return answer


def question_one_b():
    """Run question one-b."""
    # Do not edit this function
    space = " "
    question_one_output_b = str(compute_square(10))
    question_one_output_b = question_one_output_b + space + str(compute_square(-10))
    question_one_output_b = question_one_output_b + space + str(compute_square(0))
    return question_one_output_b


# }}}

# TODO: Question 1c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function compute_summation should:
# --> Accept as input an int value called maximum
# --> Produce as output an int that is the summation
# of all the values from 1 to the maximum-1
# --> For instance, if the function receives 5 as
# input it would perform the computation 1+2+3+4 and
# return the int value of 10 as output.


def compute_summation(value: int) -> int:
    """Compute the summation of the first value numbers."""
    return int(value)


def question_one_c():
    """Run question one-c."""
    # Do not edit this function
    space = " "
    question_one_output_c = str(compute_summation(5))
    question_one_output_c = question_one_output_c + space + str(compute_summation(6))
    question_one_output_c = question_one_output_c + space + str(compute_summation(7))
    return question_one_output_c


# }}}

# Do not edit any of the source code below this line

def run_question_one():
    """Run all of the subquestions in question one."""
    # call the function for question one-a
    output = question_one_a()
    print(output)
    # call the function for question one-b
    output = question_one_b()
    print(output)
    # call the function for question one-c
    output = question_one_c()
    print(output)


if __name__ == "__main__":
    run_question_one()
