def arithmetic_arranger(problems, show_answers=False):
    # Beginning of valid problem check
    counter = 0
    # Checking that number of problems does not exceed 5
    if len(problems) > 5:
        return "Error: Too many problems."
    # Checking that valid operators are in the problem
    for problem in problems:
        if problem.find("+") == -1 and problem.find("-") == -1:
            return "Error: Operator must be '+' or '-'."
    # Checking that individual numbers are not bigger than 4 digits and that the problem contains no invalid characters.
    for problem in problems:
        has_invalid_char = False
        for char in problem:
            if char.isnumeric():
                counter += 1
            else:
                counter = 0
            if counter > 4:
                break
            if not (char.isnumeric() or char.isspace() or char == "+" or char == "-"):
                has_invalid_char = True
                break
        if counter > 4:
            return "Error: Numbers cannot be more than four digits."
        if has_invalid_char:
            return "Error: Numbers must only contain digits."
        counter = 0
    # End of valid problem check

    top = ""
    bottom = ""
    dashes = ""
    results = ""
    # Seperate strings to concatenate later
    # Keep count of i to add spaces if not first problem
    for i, problem in enumerate(problems):
        left, operator, right = problem.split()
        width = max(len(left), len(right)) + 2

        top_part = left.rjust(width)
        bottom_part = operator + right.rjust(width - 1)
        dash_part = "-" * width

        if operator == "+":
            answer = str(int(left) + int(right))
        elif operator == "-":
            answer = str(int(left) - int(right))

        result_part = answer.rjust(width)

        if i > 0:
            top += "    "
            bottom += "    "
            dashes += "    "
            results += "    "

        top += top_part
        bottom += bottom_part
        dashes += dash_part
        results += result_part

    if show_answers:
        return top + "\n" + bottom + "\n" + dashes + "\n" + results
    else:
        return top + "\n" + bottom + "\n" + dashes

# Here is where you can change the problems you want to format
print(f'\n{arithmetic_arranger(["743 - 698", "4041 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')