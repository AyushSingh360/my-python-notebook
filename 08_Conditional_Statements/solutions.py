# Solutions – Conditional Statements

# ==========================================
# Easy
# ==========================================

# 1. Even or Odd
# ------------------------------------------
def exercise_1(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 2. Age Check
# ------------------------------------------
def exercise_2(age):
    return "Adult" if age >= 18 else "Minor"

# 3. Vowel Check
# ------------------------------------------
def exercise_3(char):
    return char.lower() in "aeiou"

# Test Easy
print(f"10 is {exercise_1(10)}")
print(f"Age 15 is {exercise_2(15)}")
print(f"Is 'A' vowel? {exercise_3('A')}")


# ==========================================
# Medium
# ==========================================

# 4. Grading System
# ------------------------------------------
def exercise_4(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

print(f"Score 85: {exercise_4(85)}")

# 5. Traffic Light
# ------------------------------------------
def exercise_5(light_color):
    color = light_color.lower()
    if color == "red": return "Stop"
    elif color == "yellow": return "Caution"
    elif color == "green": return "Go"
    else: return "Invalid"

print(f"Green light: {exercise_5('Green')}")

# 6. Access Control
# ------------------------------------------
def exercise_6(is_admin, is_active, has_permission):
    if is_admin and is_active and has_permission:
        return "Access Granted"
    return "Access Denied"


# ==========================================
# Hard
# ==========================================

# 7. Loan Eligibility
# ------------------------------------------
def exercise_7(age, income, credit_score):
    if age >= 18:
        if income >= 30000 or credit_score >= 700:
            return "Approved"
    return "Denied"

print(f"Loan: {exercise_7(25, 25000, 720)}")

# 8. Numeric Categorization
# ------------------------------------------
def exercise_8(n):
    # Sign part
    if n > 0:
        sign = "Positive"
        # Nested size check
        if n < 10: size = "Small"
        elif n <= 100: size = "Medium"
        else: size = "Large"
    elif n < 0:
        sign = "Negative"
        size = "N/A"
    else:
        sign = "Zero"
        size = "N/A"
        
    return (sign, size)

print(f"Cat 50: {exercise_8(50)}")

# 9. Command Parser
# ------------------------------------------
def exercise_9(command_str):
    if not command_str:
        return "Empty command"
        
    parts = command_str.split()
    op = parts[0]
    
    if op == "add":
        # Check if item arg exists
        if len(parts) > 1:
            return f"Adding {parts[1]}"
        else:
            return "Unknown command" # or distinct error like "Missing item"
    elif op == "remove":
        if len(parts) > 1:
            return f"Removing {parts[1]}"
        else:
            return "Unknown command"
    elif op == "list":
        return "Listing items"
    else:
        return "Unknown command"

print(f"Cmd: {exercise_9('add apples')}")

# 10. Rock Paper Scissors
# ------------------------------------------
def exercise_10(player_choice, cpu_choice):
    p = player_choice.lower()
    c = cpu_choice.lower()
    
    if p == c:
        return "Draw"
    
    # Winning conditions
    if (p == "rock" and c == "scissors") or \
       (p == "scissors" and c == "paper") or \
       (p == "paper" and c == "rock"):
       return "Win"
       
    return "Lose"

print(f"RPS (R vs S): {exercise_10('rock', 'scissors')}")
