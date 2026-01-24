# Exercises – Conditional Statements
# Fill in the code blocks below to solve the exercises.

# ==========================================
# Easy
# ==========================================

def exercise_1(n):
    """
    1. Check if the number `n` is even or odd.
    2. Return the string "Even" or "Odd".
    """
    # Write your code here
    pass

def exercise_2(age):
    """
    Check the age:
    - If age < 18, return "Minor"
    - If age >= 18, return "Adult"
    """
    # Write your code here
    pass

def exercise_3(char):
    """
    Check if the logical character `char` (str length 1) is a vowel (a, e, i, o, u).
    Return True if it is, False otherwise. Case-insensitive.
    """
    # Write your code here
    pass


# ==========================================
# Medium
# ==========================================

def exercise_4(score):
    """
    Implement a grading system:
    - 90-100: "A"
    - 80-89: "B"
    - 70-79: "C"
    - 60-69: "D"
    - Below 60: "F"
    Return the grade.
    """
    # Write your code here
    pass

def exercise_5(light_color):
    """
    Traffic Light Simulator.
    - "red" -> "Stop"
    - "yellow" -> "Caution"
    - "green" -> "Go"
    - Any other input -> "Invalid"
    Input should be case-insensitive.
    """
    # Write your code here
    pass

def exercise_6(is_admin, is_active, has_permission):
    """
    Check access. Return "Access Granted" ONLY if:
    - User is an admin
    - AND User is active
    - AND User has permission
    Otherwise return "Access Denied"
    """
    # Write your code here
    pass


# ==========================================
# Hard
# ==========================================

def exercise_7(age, income, credit_score):
    """
    Loan Eligibility Check:
    - Approved if: (Age >= 18) AND (Income >= 30000 OR Credit Score >= 700)
    - Otherwise "Denied"
    Return "Approved" or "Denied"
    """
    # Write your code here
    pass

def exercise_8(n):
    """
    Categorize the number `n`:
    - First check sign: "Positive", "Negative", "Zero"
    - IF Positive: also check size: "Small" (<10), "Medium" (10-100), "Large" (>100)
    
    Return a tuple: (sign_category, size_category)
    Note: size_category for Negative/Zero can be None or "N/A"
    """
    # Write your code here
    pass

def exercise_9(command_str):
    """
    Simple Command Parser.
    Parse the string `command_str` (e.g., "add item").
    - If starts with "add": return "Adding <item>"
    - If starts with "remove": return "Removing <item>"
    - If "list": return "Listing items"
    - If empty string or None: return "Empty command"
    - Otherwise: "Unknown command"
    """
    # Write your code here
    pass

def exercise_10(player_choice, cpu_choice):
    """
    Rock, Paper, Scissors Logic.
    Return "Win" if player wins, "Lose" if player loses, "Draw" if same.
    Standard rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
    """
    # Write your code here
    pass

if __name__ == "__main__":
    # Test your functions here
    pass
