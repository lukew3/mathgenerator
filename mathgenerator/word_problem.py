def solve_word_problem(operation):
    """
    Solves a word problem based on user-defined operation and variables.

    Parameters:
    operation (str): The arithmetic operation to perform. Can be 'addition', 'subtraction', 'multiplication', or 'division'.

    Returns:
    int: The result of the arithmetic operation.
    """
    # Mapping of short forms to full operation names
    operation_mapping = {
        'a': 'addition',
        's': 'subtraction',
        'm': 'multiplication',
        'd': 'division'
    }

    # Validate and expand the operation input if it's a short form
    operation = operation_mapping.get(operation.lower(), operation)

    print("Enter the variables:")
    variables = {}
    variables['start'] = int(input("Enter the first number: "))
    
    if operation in ['addition', 'subtraction']:
        num_variables = int(input("Enter the number of additional numbers: "))
        for i in range(num_variables):
            variables['num' + str(i+1)] = int(input("Enter number " + str(i+1) + ": "))
    elif operation in ['multiplication', 'division']:
        num_factors = int(input("Enter the number of factors: "))
        for i in range(num_factors):
            variables['factor' + str(i+1)] = int(input("Enter factor " + str(i+1) + ": "))
    else:
        print("Error: Unsupported operation.")
        return None

    if operation == 'addition':
        result = sum(variables.values())
    elif operation == 'subtraction':
        result = variables['start'] - sum(list(variables.values())[1:])
    elif operation == 'multiplication':
        result = 1
        for value in variables.values():
            result *= value
    elif operation == 'division':
        result = variables['start']
        for value in list(variables.values())[1:]:
            result /= value
    else:
        print("Error: Unsupported operation.")
        return None

    return result

# Example usage:
user_operation = input("Enter the arithmetic operation (a for addition, s for subtraction, m for multiplication, d for division): ")
result = solve_word_problem(user_operation)
print("Result of", user_operation, "is", result)
