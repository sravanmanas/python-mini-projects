# Student Grade Calculator

def calculate_grade(marks):
    # Assign grade based on marks range
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F (Fail)"

def main():
    print("===== Student Grade Calculator =====")
    
    # Take user inputs
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))
    
    # Calculate grade
    grade = calculate_grade(marks)
    
    # Display results
    print(f"\nStudent: {name}")
    print(f"Marks: {marks}/100")
    print(f"Percentage: {marks}%")
    print(f"Grade: {grade}")
main()
