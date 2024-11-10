import random

def generate_random_integer(min_value, max_value):
        return random.randint(min_value, max_value)

def generate_random_operator():
    return random.choice(['+', '-', '*'])

def evaluate_expression(n1, n2, operator):
    # Create the problem string (e.g., "5 + 3")
    problem = f"{n1} {operator} {n2}"
    
   
    if operator == '+':
        answer = n1 + n2  # Addition
    elif operator == '-':
        answer = n1 - n2  # Subtraction
    else:
        answer = n1 * n2  # Multiplication
    
    
    return problem, answer

def math_quiz():
    # Initialize score
    score = 0
    total_questions = 5  # Total number of questions to ask

  
    print("Welcome to the Math Quiz Game!")

    
    for _ in range(total_questions):
        # Generate random numbers and operator for the current question
        num1 = generate_random_integer(1, 10)  # Random number 1
        num2 = generate_random_integer(1, 10)  # Random number 2
        operator = generate_random_operator()  # Random operator (+, -, or *)

        # Generate the math problem and the correct answer
        problem, correct_answer = evaluate_expression(num1, num2, operator)
        
        # Print the math problem 
        print(f"Question: {problem}")
        
        # Error handling 
        while True:
            try:
                # Get the user's answer and try to convert it to an integer
                user_answer = int(input("Your answer: "))
                break  # Exit the loop if conversion is successful
            except ValueError:
                # If conversion fails, print an error message and ask again
                print("Invalid input! Please enter a valid number.")

        # Check if the user's answer is correct
        if user_answer == correct_answer:           
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
