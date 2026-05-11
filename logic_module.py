from input_module import details_input

def calculate_grade():
    try:
        score = details_input()
        
        if score < 0 or score > 100:
            print("Enter a valid score")
        elif score >= 40:
            print("You pass")
        else:
            print("You Fail")
    except Exception as e:
        print(f"Error: {e}")