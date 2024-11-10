import random

def generate_random_integer(min, max):
    """
    Generate a random integer between min_value and max_value.
    
    Parameters:
    min_value (int): The minimum value for the random integer.
    max_value (int): The maximum value for the random integer.
    
    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Randomly select an arithmetic operator from a list of '+', '-', and '*'.
    
    Returns:
    str: A random arithmetic operator.
    """
    return random.choice(['+', '-', '*']


def evaluate_expression(n1, n2, operator):
    """
    Evaluate a mathematical expression based on the operator.
    
    Parameters:
    n1 (int): The first number in the expression.
    n2 (int): The second number in the expression.
    operator (str): The arithmetic operator ('+', '-', or '*').
    
    Returns:
    tuple: A tuple containing the string representation of the problem and the correct answer.
    """
    problem = f"{n1} {operator} {n2}"
    
    # Perform the calculation based on the operator
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 5  # Fixed to an integer value for the number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Ask the user 5 questions (total_questions)
    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)  # Changed from 5.5 to 10 for consistency in integers
        operator = generate_random_operator()

        # Generate the problem and get the correct answer
        problem, correct_answer = evaluate_expression(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        
        # Error handling for user input
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)  # Convert the input to an integer
                break  # Exit the loop if conversion is successful
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Print the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
