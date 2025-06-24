#!/usr/bin/env python3
import mathgenerator
import sys


def main():
    """
    Run a mathgenerator function by name and print the output.
    
    Usage: python mg.py <function_name>
    Example: python mg.py addition
    """
    if len(sys.argv) != 2:
        print("Usage: python mg.py <function_name>")
        print("Example: python mg.py addition")
        sys.exit(1)
    
    function_name = sys.argv[1]
    
    try:
        # Get the function from the mathgenerator module
        func = getattr(mathgenerator, function_name)
        
        # Call the function and get the result
        result = func()
        
        # Print the result
        print(result)
        
    except AttributeError:
        print(f"Error: Function '{function_name}' not found in mathgenerator module")
        print("Available functions can be found by checking mathgenerator.get_gen_list()")
        sys.exit(1)
    except Exception as e:
        print(f"Error calling function '{function_name}': {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
