"""Question five for an executable examination."""


# TODO: Question 5a. {{{

# Instructions:
# Implement the requested function so that it operates in the specified fashion

# Function description:
# The function compute_cube should:
# --> Accept as input one int value called input_one
# --> Using any appropriate approach compute and return the cube of that number
# --> For instance, if value_one is equal to 10 and value_two is
#     equal to 2 then this function would return the remainder of 0
# --> Alternatively, if value_one is equal to 10 and value_two is
#     equal to 3 then this function would return the remainder of 1


def compute_cube(input_one: int) -> int:
    """Compute the cube of an input number."""
    return input_one


def question_five_a():
    """Run question five-a."""
    # Do not edit this function
    space = " "
    question_five_output_a = str(compute_cube(1))
    question_five_output_a = question_five_output_a + space + str(compute_cube(2))
    question_five_output_a = question_five_output_a + space + str(compute_cube(3))
    return question_five_output_a


# }}}

# TODO: Question 5b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function get_maximum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is greater than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two


def get_maximum(input_one: int, input_two: int) -> int:
    """Return the maximum value of two input values."""
    input_one = 0
    if input_one >= input_two:
        return input_two
    return input_one


def question_five_b():
    """Run question five-b."""
    # Do not edit this function
    space = " "
    question_five_output_b = str(get_maximum(12, 10))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 9))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 3))
    return question_five_output_b

# }}}

# TODO: Question 5c. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function get_minimum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is less than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two


def get_minimum(input_one: int, input_two: int) -> int:
    """Return the minimum value of two input values."""
    input_one = input_two
    if input_one <= input_two:
        return False
    return True


def question_five_c():
    """Run question five-b."""
    # Do not edit this function
    space = " "
    question_five_output_b = str(get_minimum(12, 10))
    question_five_output_b = question_five_output_b + space + str(get_minimum(3, 9))
    question_five_output_b = question_five_output_b + space + str(get_minimum(2, 2))
    return question_five_output_b

# }}}


# Do not edit any of the source code below this line


def run_question_five():
    """Run all of the subquestions in question five."""
    # call the function for question five-a
    output = question_five_a()
    print(output)
    # call the function for question five-b
    output = question_five_b()
    print(output)
    # call the function for question five-c
    output = question_five_c()
    print(output)


if __name__ == "__main__":
    run_question_five()
