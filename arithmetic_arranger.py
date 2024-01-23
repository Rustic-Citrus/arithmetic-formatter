def arithmetic_arranger(problems: list, show_answer: bool = False):
    lines = [list() for n in range(4)]
    arranged_problems = []

    # Raise an exception if there are more than 5 problems.
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Split the problems into their integers and operators.
        problem_parts = problem.split(" ")
        
        # Find the length of the operands.
        operand_one_len = len(problem_parts[0])
        operand_two_len = len(problem_parts[2])
        max_operand_len = max(operand_one_len, operand_two_len)

        # Raise an exception if either of the operands is longer than 4 digits.
        if (operand_one_len > 4) or (operand_two_len > 4):
            return "Error: Numbers cannot be more than four digits."

        # Set the maximum width for each problem.
        problem_width = max_operand_len + 2

        # Convert the operands from strings to integers.
        try:
            operand_one = int(problem_parts[0])
            operand_two = int(problem_parts[2])

        # Raise an exception if the operands are not numbers.
        except ValueError:
            return "Error: Numbers must only contain digits."

        # Identify the operator and calculate the solution.
        operator = problem_parts[1]
        solution = 0
        if operator == "+":
            solution = operand_one + operand_two
        elif operator == "-":
            solution = operand_one - operand_two

        # Raise an exception if the operator is not '+' or '-'.
        elif (operator != "+") and (operator != "-"):
            return "Error: Operator must be '+' or '-'."
        
        lines[0].append((" " * (problem_width - operand_one_len) + str(operand_one) + (" " * 4)))
        lines[1].append(operator + (" " * (problem_width - operand_two_len - 1)) + str(operand_two) + (" " * 4))
        lines[2].append(("-" * problem_width) + (" " * 4))
        lines[3].append((" " * (problem_width - len(str(solution))) + str(solution) + (" " * 4)))

    # If True was passed as a second argument, drop the solution line.
    if not show_answer:
        lines.pop()

    # Remove added whitespace on the right side of each line.
    for line in lines:
        line[-1] = line[-1].rstrip()

    # Append a line break to the end of every line except the last.
    for line in lines[:-1]:
        line.append("\n")

    # Concatenate the strings horizontally to form lines.
    for line in lines:
        arranged_problems.append("".join(line))

    # Concatenate the lines to form one continuous string.
    arranged_problems = "".join(arranged_problems)

    return arranged_problems


def user_test():
    def show_answer():
        user_input_04 = input("Would you like to show the answers? (Y/N) ")
        try:
            if user_input_04.upper() == "Y":
                print(arithmetic_arranger(list_of_equations, True))
            else:
                print(arithmetic_arranger(list_of_equations))
        except Exception as e:
            print("Error: Some equations were not formatted correctly.")

    goodbye_output = "Thank you for your time."

    user_input_01 = input("Would you like to test the function yourself? (Y/N) ")
    if user_input_01.upper() == "N":
        print(goodbye_output)
    elif user_input_01.upper() == "Y":
        print("You can type up to 5 equations.")
        print("The correct format for the equation is as follows,")
        print("where 'n' represents a number of 4 digits or less:")
        print("'n1 + n2' or 'n1 - n2'.")
        print("If you want to type fewer than 5 equations,")
        print("type 'done'.")
        done = False
        list_of_equations = []
        user_input_02 = input("Type an equation in the correct format: ")
        while not done:
            if user_input_02.lower() == "done":
                if len(list_of_equations) == 0:
                    print("You didn't type any equations.")
                    user_input_03 = input("Are you sure you are done? (Y/N) ")
                    if user_input_03.upper() == "Y":
                        done = True
                else:
                    show_answer()
                    done = True
            elif len(list_of_equations) <= 4:
                list_of_equations.append(user_input_02)
                print(f"{user_input_02} added to list of equations.")
                if len(list_of_equations) == 5:
                    print("You have reached the maximum number of equations.")
                    show_answer()
                    done = True
                else:
                    user_input_02 = input("Type an equation in the correct format: ")
            elif len(list_of_equations) >= 5:
                print("You have reached the maximum number of equations.")
                show_answer()
                done = True
        print(goodbye_output)
    else:
        print(f"'{user_input_01}' not recognised as 'Y' or 'N'.")
        print("Assuming 'No'.")