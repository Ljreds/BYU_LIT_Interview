
def reverse_string(str):
    """Return the reverse of the given string using slicing."""
    return str[::-1]

def sum_of_three(first_number, second_number, third_number):
    """Return the sum of three numbers."""

    sum = 0
    number_list  = [first_number, second_number, third_number]
    for i in number_list:
        sum = sum + i
    return sum

def recursive_factorial(num):
    """
    Compute factorial of a positive integer using recursion.
    Example: 5! = 5 * 4 * 3 * 2 * 1
    """
    if(num == 1):
        return 1
    else:
        # Recursive step: multiply n by factorial of (n - 1)
        factorial = num * recursive_factorial(num - 1)
    
    return factorial

def fibonacci_sequence(num):
    """
    Return the nth Fibonacci number using recursion.
    n must be a positive integer.
    """

    count = num - 1
    sum = 0
    sequence_1 = 0
    sequence_2 = 1
    if(num == 1): # special case: first Fibonacci number
        return 1
    else:
        while(count > 0):
            sum = sequence_1 + sequence_2
            sequence_1 = sequence_2
            sequence_2 = sum

            count -= 1 
    
    return sum


def main():

    command = input("Enter a command. Type 'help' for a list of commands: ")

    match command:
        case '-r':
            s = input("Enter a string: ")
            print(reverse_string(s))
        case '-a':
            print("The sum of three numbers")
            first_number = int(input("Enter the first number: "))
            second_number = int(input("Enter the second number: "))
            third_number = int(input("Enter the third number: "))
    
            print(sum_of_three(first_number, second_number, third_number))
            return
        case '-f':
            print("The factorial of a number")
            try:
                factorial_number = int(input("Enter a positve number: "))
            except ValueError:
                # Catches an error caused by invalid integer input
                print("Not an integer") 
                return
            
            if(factorial_number < 0):
                print("That is not a positive number")
                return
            else:
                print(recursive_factorial(factorial_number))
                return
        case '-s':
            print("The Nth entry of the fibonacci sequence")
            fibonacci_number = int(input("Enter a positive number: "))

            try:
                fibonacci_number = int(input("Enter a positve number: "))
            except ValueError:
                # Catches an error caused by invalid integer input
                print("Not an integer") 
                return
            
            if(factorial_number < 0):
                print("That is not a positive number")
                return
            else:
                print(fibonacci_sequence(fibonacci_number))
                return
        case 'help':
            print(
                "List of commands:\n"
                "-r: Takes in a string and reverses it\n"
                "-a: Takes in three numbers and adds them together\n"
                "-f: Return factorial of an inputed number\n"
                "-s: Returns the nth entry of the fibonacci sequence\n"
                "help: Prints this message\n"
            )
            main()
        case _:
            print("Invalid command. Type 'help' for a list of commands.")
            main()













if __name__ == "__main__":
    main()
